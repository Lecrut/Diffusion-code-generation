def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

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
        }
    }

    flat_organization = flatten_dict(organization)
    print(flat_organization)