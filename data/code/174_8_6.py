if __name__ == '__main__':
    organization = {
        "CEO": {
            "name": "Alice Smith",
            "departments": {
                "Engineering": {
                    "manager": "Bob Johnson",
                    "employees": {
                        "Engineer1": {"title": "Software Engineer", "salary": 90000},
                        "Engineer2": {"title": "Senior Software Engineer", "salary": 110000}
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
            "manager": "Diana Prince",
            "employees": {
                "HR_Specialist": {"title": "HR Manager", "salary": 75000}
            }
        }
    }
    print("--- Organization Structure ---")
    print(f"CEO: {organization['CEO']['name']}")
    engineering = organization['CEO']['departments']['Engineering']
    print("\nEngineering Department:")
    print(f"Manager: {engineering['manager']}")
    for emp_id, details in engineering['employees'].items():
        print(f"- {emp_id}: {details['title']}, Salary: ${details['salary']}")
    marketing = organization['CEO']['departments']['Marketing']
    print("\nMarketing Department:")
    print(f"Manager: {marketing['manager']}")
    for emp_id, details in marketing['employees'].items():
        print(f"- {emp_id}: {details['title']}, Salary: ${details['salary']}")
    hr = organization['HR']
    print("\nHR Department:")
    print(f"Manager: {hr['manager']}")
    for emp_id, details in hr['employees'].items():
        print(f"- {emp_id}: {details['title']}, Salary: ${details['salary']}")