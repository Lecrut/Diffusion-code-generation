def search_employee(directory: list[dict], target_name: str) -> int | None:
    for index, employee in enumerate(directory):
        if employee.get("name") == target_name:
            return index
    return None
if __name__ == '__main__':
    employees = [
        {"id": 101, "name": "Alice Johnson", "role": "Engineer"},
        {"id": 102, "name": "Bob Smith", "role": "Designer"},
        {"id": 103, "name": "Charlie Brown", "role": "Manager"},
    ]
    target = "Alice Johnson"
    result_index = search_employee(employees, target)
    if result_index is not None:
        print(f"{target} found at index {result_index}")
    else:
        print(f"{target} not found")