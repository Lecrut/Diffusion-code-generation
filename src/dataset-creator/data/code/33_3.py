def search_employee_directory(name):
    employees = [
        {"id": 101, "name": "Alice Johnson", "role": "Engineer"},
        {"id": 102, "name": "Bob Smith", "role": "Manager"},
        {"id": 103, "name": "Charlie Brown", "role": "Designer"}
    ]
    result = [emp for emp in employees if name.lower() in emp["name"].lower()]
    return result
if __name__ == '__main__':
    target_name = "Alice"
    found_employees = search_employee_directory(target_name)
    if len(found_employees) > 0:
        print(f"{target_name} was found.")
        for emp in found_employees:
            print(emp["name"])
    else:
        print("Not Found")