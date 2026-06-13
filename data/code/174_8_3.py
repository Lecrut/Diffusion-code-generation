if __name__ == '__main__':
    organization = {
        "CEO": {
            "name": "Alice Smith",
            "departments": {
                "Engineering": {
                    "manager": "Bob Johnson",
                    "employees": {
                        "Engineer1": {"title": "Software Engineer", "salary": 80000},
                        "Engineer2": {"title": "Senior Software Engineer", "salary": 100000}
                    }
                },
                "Marketing": {
                    "manager": "Charlie Brown",
                    "employees": {
                        "Marketer1": {"title": "Marketing Specialist", "salary": 65000}
                    }
                }
            }
        },
        "HR": {
            "name": "Diana Prince",
            "departments": {
                "Recruitment": {
                    "manager": "Eve Adams",
                    "employees": {
                        "Recruiter1": {"title": "Recruiter", "salary": 70000}
                    }
                }
            }
        }
    }
    print("--- Organization Structure ---")
    print(f"CEO: {organization['CEO']['name']}")
    print("\nDepartments under CEO:")
    for dept_name, dept_data in organization['CEO']['departments'].items():
        print(f"- {dept_name}: Manager is {dept_data['manager']}")
        print("  Employees:")
        for emp_name, emp_details in dept_data['employees'].items():
            print(f"    {emp_name}: {emp_details['title']} (Salary: ${emp_details['salary']})")
    print("\nHR Department:")
    hr_data = organization['HR']
    print(f"HR Manager: {hr_data['name']}")
    for dept_name, dept_data in hr_data['departments'].items():
        print(f"- {dept_name}: Manager is {dept_data['manager']}")