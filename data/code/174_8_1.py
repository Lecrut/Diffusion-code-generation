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
    print("Organization Structure:")
    import json
    print(json.dumps(organization, indent=4))