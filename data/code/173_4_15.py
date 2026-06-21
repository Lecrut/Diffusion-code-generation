import operator

def group_by_attribute(objects, attr):
    grouped = {}
    for obj in objects:
        key = getattr(obj, attr)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(obj)
    return grouped

if __name__ == '__main__':
    class Employee:
        def __init__(self, name, department):
            self.name = name
            self.department = department
    
    employees = [
        Employee("Alice", "Engineering"),
        Employee("Bob", "HR"),
        Employee("Charlie", "Engineering"),
        Employee("David", "Marketing")
    ]
    
    grouped_by_department = group_by_attribute(employees, 'department')
    print(grouped_by_department)