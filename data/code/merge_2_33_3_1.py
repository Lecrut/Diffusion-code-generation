def search_employee(directory: list[dict], target_name: str) -> dict | None:
    for employee in directory:
        if employee.get('name') == target_name:
            return employee
    return None
if __name__ == '__main__':
    employees = [
        {'id': 1, 'name': 'Alice Johnson', 'role': 'Engineer'},
        {'id': 2, 'name': 'Bob Smith', 'role': 'Designer'},
        {'id': 3, 'name': 'Charlie Brown', 'role': 'Manager'}
    ]
    target = "Alice Johnson"
    result = search_employee(employees, target)
    if result:
        print(f"Found {target}:")
        for key in ['id', 'name', 'role']:
            print(f"{key.capitalize()}: {result[key]}")
    else:
        print(f"No employee found named {target}")