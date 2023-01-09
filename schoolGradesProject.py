import pandas as pd
import time
# -----------------------------------------------------------------------------
# student class -> base for all student objects
class Student:
    def __init__(self, name):
        self.name = name

    grade1 = None
    grade2 = None
    recovery = None

    def needRecovery(self):
        if self.calculateAverage() < 6:
            return True

    def calculateAverage(self):
        average = (self.grade1 + self.grade2) / 2
        return average
     
    def calculateAverageAfterRecovery(self):
        average = (self.calculateAverage() + self.recovery) / 2
        return average

    def isAproved(self):
        if self.calculateAverage() >= 6:
            return "Aprovado"
        elif self.calculateAverageAfterRecovery() >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

# -----------------------------------------------------------------------------
# student list and a method to check if a student needs recovery
students = []
def checkStudentNeedsRecovery():
    global students
    for student in students:
        if student.needRecovery():
            return True
    return False

# -----------------------------------------------------------------------------
# system starts and asks for the ammount of students
print("------Bem vindo ao sistema-------")
studentsNumber = None
while type(studentsNumber) is not int:
    try:
        studentsNumber = int(input("Informe a quantidade de estudantes: "))
    except:
        print("Digite um número!\n")

# -----------------------------------------------------------------------------
# asks for the student names and creates an object with them
print("\n----Preciso que informe o nome dos alunos----")
id = 1
for i in range(studentsNumber):
    name = None
    while not name:
        name = input(str(id) + "-Infome o nome do aluno: ")
    student = Student(name)
    students.append(student)
    id += 1
print("Alunos Inseridos com sucesso! \n")

# -----------------------------------------------------------------------------
# asks for the students grades and creates an attribute with them
print("---Preciso que informe a nota dos alunos---")
for student in students:
    grade1, grade2 = None, None
    while True:
        try:
            grade1 = float(input(f"Informe a nota no 1° Semestre do aluno {student.name}: "))
        except:
            print("Digite um número!\n")
        try:
            grade2 = float(input(f"Informe a nota no 2° Semestre do aluno {student.name}: "))
        except:
            print("Digite um número!\n")

        if grade1 and grade2:
            break

    student.grade1 = round(grade1, 2)   # rounds the float value
    student.grade2 = round(grade2, 2)   # rounds the float value
    print()

# -----------------------------------------------------------------------------
# displays the students grades
print("-------Notas dos alunos-------")
data = {
  "Aluno": [student.name for student in students],
  "1° Tri": [student.grade1 for student in students],
  "2° Tri": [student.grade2 for student in students],
  "Média": [student.calculateAverage() for student in students]
}
table = pd.DataFrame(data)
print(table)

# -----------------------------------------------------------------------------
# checks if any of the students needs recovery and displays their name
if checkStudentNeedsRecovery():
    print("\n------Alunos que precisam de recuperação------")
    data = {
        "Aluno": [student.name for student in students if student.needRecovery()],
        "Média": [student.calculateAverage() for student in students if student.needRecovery()],
        "Precisa de recuperação": ["SIM" for student in students if student.needRecovery()]
        }
    table = pd.DataFrame(data)
    print(table)
    ciente = input("\n                                 | CIENTE | ")
        
# -----------------------------------------------------------------------------
# in case of the students who needs recovery the system asks if the user is willing to type their recovery grade
    choice = None
    while choice not in ["S"]:
        choice = input("\nDeseja informar a nota dos alunos que ficaram de recuperação? (S/N): ").upper()
        if choice == "N":
            print("Ok! Informe as notas assim que puder!\n")
            time.sleep(5)

# -----------------------------------------------------------------------------
# asks the recovery grade of the students who need it
    print("")
    if choice == "S": 
        for student in students:
            if student.needRecovery():
                while True:
                    recovery = None
                    try:
                        recovery = float(input(f"Informe a nota de recuperação do aluno {student.name}: "))
                    except:
                        print("Digite um número!\n")
                    if recovery:
                        break
                student.recovery = round(recovery, 2)

# -----------------------------------------------------------------------------
# displays the final school report
print("\n------------Boletim Escolar------------")
data = {
    "Aluno": [student.name for student in students],
    "1° Tri": [student.grade1 for student in students],
    "2° Tri": [student.grade2 for student in students],
    "Recuperação": [student.recovery if student.needRecovery() else "n/precisa" for student in students],
    "Média": [student.calculateAverage() if not student.needRecovery() else student.calculateAverageAfterRecovery() for student in students],
    "Situação": [student.isAproved() for student in students]
}
table = pd.DataFrame(data)
print(table)