def get_max_salary(employees):
    if not employees:
        return None
    max_sal = employees[0].get('salary')
    if max_sal is None:
        raise ValueError("First employee missing salary")
    for emp in employees:
        sal = emp.get('salary')
        if sal is not None and sal > max_sal:
            max_sal = sal
    return max_sal

if __name__ == '__main__':
    data = [
        {"name": "Alice", "salary": 50000},
        {"name": "Bob", "salary": 65000},
        {"name": "Charlie", "salary": 45000},
        {"name": "Diana", "salary": 72000}
    ]
    print(get_max_salary(data))