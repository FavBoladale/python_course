employee_files = open("employee.txt", "r")
for employee in employee_files.readlines():
    print(employee)
employee_files.close()