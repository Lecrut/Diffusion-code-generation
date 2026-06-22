def get_max_salary(employees):
    return max((emp.get('salary', 0) for emp in employees), default=0)

if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 55000}
    ]
    print(get_max_salary(data))