def search_employee(directory, target_name):
    matching_employees = [emp for emp in directory if (emp['first'] == target_name or emp['last'] == target_name)]
    return matching_employees
def main():
    employee_directory = [
        {'id': 1, 'first': 'John', 'last': 'Doe'},
        {'id': 2, 'first': 'Jane', 'last': 'Smith'},
        {'id': 3, 'first': 'Bob', 'last': 'Johnson'},
        {'id': 4, 'first': 'Alice', 'last': 'Williams'}
    ]
    target_name = "Doe"
    results = search_employee(employee_directory, target_name)
    if not results:
        print(f"No employees found with the name '{target_name}'.")
    else:
        print(f"Found {len(results)} employee(s):")
        for emp in results:
            print(f"- ID: {emp['id']}, Name: {emp['first']} {emp['last']}")
if __name__ == '__main__':
    main()