from collections import defaultdict
from typing import List, NamedTuple

class Employee(NamedTuple):
    id: int
    department: str
    name: str

def group_employees_by_department(employees: List[Employee]) -> dict:
    groups = defaultdict(list)
    for emp in employees:
        groups[emp.department].append(emp)
    return dict(groups)

if __name__ == '__main__':
    sample_employees = [
        Employee(id=1, department='HR', name='Alice'),
        Employee(id=2, department='Engineering', name='Bob'),
        Employee(id=3, department='HR', name='Charlie'),
        Employee(id=4, department='Marketing', name='David'),
    ]
    print(group_employees_by_department(sample_employees))