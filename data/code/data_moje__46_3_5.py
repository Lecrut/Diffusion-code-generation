employees = [{'name': 'Alice', 'salary': 75000}, {'name': 'Bob', 'salary': '82000'}, {'name': 'Charlie', 'salary': 68000.5}]
def get_max_salary(records):
    return max(map(lambda x: float(x['salary']) if isinstance(x.get('salary'), (int, float, str)) else float('-inf'), records))
if __name__ == '__main__':
    print(get_max_salary(employees))