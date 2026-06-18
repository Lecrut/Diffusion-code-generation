def search_employee(directory, target_name):
    results = [employee['name'] for employee in directory if 'name' in employee and target_name.lower() == employee['name'].lower()]
    if not results:
        print(f"No records found matching '{target_name}'.")
        return None
    first_match = results[0]
    print(f"Record found for {first_match}.")
    employee_details = [employee['name'] + " - " + str(employee.get('id', 'N/A')) 
                       for employee in directory if target_name.lower() == employee.get('name', '').lower()]
    return employee_details
if __name__ == '__main__':
    employees = [
        {'name': 'Alice Johnson', 'id': 101, 'department': 'HR'},
        {'name': 'Bob Smith', 'id': 102, 'department': 'IT'},
        {'name': 'Charlie Brown', 'id': 103, 'department': 'Marketing'},
    ]
    target = "Alice Johnson"
    found_records = search_employee(employees, target)