class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age})"

def sort_employees(employees):
    return sorted(employees, key=lambda emp: emp.age)

if __name__ == '__main__':
    employees = [
        Employee("Alice", 30),
        Employee("Bob", 25),
        Employee("Charlie", 35)
    ]
    sorted_employees = sort_employees(employees)
    print(sorted_employees)