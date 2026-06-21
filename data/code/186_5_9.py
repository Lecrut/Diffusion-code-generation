class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name}: ${self.salary}"

def sort_employees(employees):
    return sorted(employees, key=lambda employee: employee.salary)

if __name__ == '__main__':
    employees = [
        Employee("Alice", 50000),
        Employee("Bob", 40000),
        Employee("Charlie", 60000)
    ]
    sorted_employees = sort_employees(employees)
    print(sorted_employees)