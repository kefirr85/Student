grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
x = 0
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
#students_list = list(sorted(students))
y = 0
for i in grades:
    print((students_list[y]), ((sum(grades[x]) / len(grades[x]))))
    x += 1
    y += 1