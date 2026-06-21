class Employee:
    def __init__(self, name, years_of_experience):
        self.name = name
        self.years_of_experience = years_of_experience
    
    def __repr__(self):
        return f"Employee(name={self.name}, experience={self.years_of_experience})"

def sort_employees_by_experience(employees):
    return sorted(employees, key=lambda employee: employee.years_of_experience)

if __name__ == '__main__':
    employees = [
        Employee("John Doe", 10),
        Employee("Jane Smith", 5),
        Employee("Alice Johnson", 7)
    ]
    sorted_employees = sort_employees_by_experience(employees)
    print(sorted_employees)