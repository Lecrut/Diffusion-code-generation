class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

def sort_employees_by_salary(employees):
    if not all(isinstance(emp, Employee) for emp in employees):
        raise ValueError("All elements must be instances of Employee")
    
    sorted_employees = sorted(employees, key=lambda emp: emp.salary)
    return sorted_employees

if __name__ == '__main__':
    employees = [
        Employee("Alice", 50000),
        Employee("Bob", 75000),
        Employee("Charlie", 60000)
    ]
    sorted_employees = sort_employees_by_salary(employees)
    print(sorted_employees)