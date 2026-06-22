import operator

def get_max_salary(employees):
    return max(map(lambda e: float(e['salary']) if isinstance(e['salary'], (int, float)) else float('-inf'), employees))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 'invalid'},
        {'name': 'Charlie', 'salary': 120000}
    ]
    print(get_max_salary(sample_data))