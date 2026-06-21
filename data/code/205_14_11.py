class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

def sort_employees_by_salary(employees):
    return sorted(employees, key=lambda emp: emp.salary)

if __name__ == '__main__':
    employees = [
        Employee("Alice", 5000),
        Employee("Bob", 4500),
        Employee("Charlie", 6000)
    ]
    sorted_employees = sort_employees_by_salary(employees)
    print(sorted_employees)