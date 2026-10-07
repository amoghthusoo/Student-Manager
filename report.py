students = [
{"Aman" : 78},
{"Rohit" : 35},
{"Sanvi" : 57},
{"Niharika" : 22},
{"Hardik" : 92}
]

def average_marks(students):
    n = len(students)

    _total = 0
    for student in students:
        marks = list(student.values())[0]
        _total += marks

    return _total/n
        

avg = average_marks(students)
print(f"The average marks are : {avg}")


print()
for student in students:
    name = list(student.keys())[0]
    marks = list(student.values())[0]

    if(marks >= 40):
        print(f"{name} : Pass")
    else:
        print(f"{name} : Fail")

import matplotlib.pyplot as plt
names = ["Aman", "Rohit", "Sanvi", "Niharika", "Hardik"]
marks = [78, 35, 57, 22, 92]

plt.bar(names, marks)
plt.xlabel("Students' Name")
plt.ylabel("Marks")
plt.title("Students' Marks")
plt.show()
