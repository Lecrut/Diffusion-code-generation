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
                    "head": "Bob Johnson",
                    "employees": {
                        "E101": "Charlie Brown",
                        "E102": "Diana Prince"
                    }
                },
                "Marketing": {
                    "head": "Eve Davis",
                    "employees": {
                        "M201": "Frank White"
                    }
                }
            }
        }
    }

    flattened = flatten_dict(organization)
    print(flattened)