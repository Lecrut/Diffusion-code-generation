def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

class DictFlattener:
    def __init__(self, nested_dict):
        self.nested_dict = nested_dict

    def flatten(self):
        return flatten_dict(self.nested_dict)

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
        }
    }

    flattener = DictFlattener(organization)
    flattened = flattener.flatten()
    print(flattened)