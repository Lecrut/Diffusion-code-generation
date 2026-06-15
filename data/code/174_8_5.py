if __name__ == '__main__':
    organization = {
        "CEO": {
            "name": "Alice Smith",
            "departments": {
                "Engineering": {
                    "manager": "Bob Johnson",
                    "employees": {
                        "Engineer 1": {"title": "Software Developer", "salary": 70000},
                        "Engineer 2": {"title": "Senior Developer", "salary": 85000}
                    }
                },
                "Marketing": {
                    "manager": "Charlie Brown",
                    "employees": {
                        "Marketer A": {"title": "Marketing Specialist", "salary": 60000}
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
                        "Recruiter 1": {"title": "Recruiter", "salary": 65000}
                    }
                }
            }
        }
    }
    print("--- Organization Structure ---")
    for department_name, dept_data in organization.items():
        print(f"\n{department_name}:")
        for key, value in dept_data.items():
            if key == "departments":
                print("  Departments:")
                for dept_name, dept_details in value.items():
                    print(f"    - {dept_name}:")
                    print(f"      Manager: {dept_details['manager']}")
                    print("      Employees:")
                    for emp_name, emp_details in dept_details['employees'].items():
                        print(f"        - {emp_name}: Title={emp_details['title']}, Salary=${emp_details['salary']}")
            else:
                print(f"  Name: {value}")