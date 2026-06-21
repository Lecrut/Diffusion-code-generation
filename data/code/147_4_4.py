class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def sort_employees_by_age(employees):
    return sorted(employees, key=lambda emp: emp.age)

if __name__ == '__main__':
    employees = [Employee("Alice", 30), Employee("Bob", 25), Employee("Charlie", 35)]
    sorted_employees = sort_employees_by_age(employees)
    for emp in sorted_employees:
        print(f"{emp.name} - {emp.age}")