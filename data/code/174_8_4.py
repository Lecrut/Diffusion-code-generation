if __name__ == '__main__':
    company_structure = {
        "CEO": {
            "name": "Alice Smith",
            "departments": {
                "Engineering": {
                    "manager": "Bob Johnson",
                    "employees": {
                        "Engineer1": {"title": "Software Engineer", "salary": 70000},
                        "Engineer2": {"title": "Senior Software Engineer", "salary": 95000}
                    }
                },
                "Marketing": {
                    "manager": "Charlie Brown",
                    "employees": {
                        "Marketer1": {"title": "Marketing Specialist", "salary": 60000}
                    }
                },
                "HR": {
                    "manager": "Diana Prince",
                    "employees": {
                        "HR_Rep1": {"title": "HR Manager", "salary": 75000}
                    }
                }
            }
        }
    }
    print("Company Structure:")
    import json
    print(json.dumps(company_structure, indent=4))