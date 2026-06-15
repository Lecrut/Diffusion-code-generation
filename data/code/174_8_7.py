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
    print("Organization Structure:")
    import json
    print(json.dumps(organization, indent=4))