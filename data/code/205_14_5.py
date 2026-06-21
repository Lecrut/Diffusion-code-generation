class Employee:
    def __init__(self, name, department, years_of_service):
        self.name = name
        self.department = department
        self.years_of_service = years_of_service

    def __repr__(self):
        return f"Employee(name={self.name}, department={self.department}, years_of_service={self.years_of_service})"

def sort_employees_by_years_of_service(employees):
    return sorted(employees, key=lambda employee: employee.years_of_service)

if __name__ == '__main__':
    employees = [
        Employee("Alice", "HR", 5),
        Employee("Bob", "Engineering", 3),
        Employee("Charlie", "Marketing", 8)
    ]
    sorted_employees = sort_employees_by_years_of_service(employees)
    print(sorted_employees)