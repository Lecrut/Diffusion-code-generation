def max_salary(employees):
    return max(map(lambda e: e.get('salary') if isinstance(e.get('salary'), (int, float)) else 0, employees))

if __name__ == '__main__':
    employees = [{'name': 'Alice', 'salary': 75000}, {'name': 'Bob', 'salary': 'N/A'}, {'name': 'Charlie', 'salary': 85000.5}]
    print(max_salary(employees))