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
        },
        "HR": {
            "head": "Grace Hall",
            "employees": {
                "H301": "Henry King"
            }
        }
    }
    print("Organization Structure:")
    import json
    print(json.dumps(organization, indent=4))