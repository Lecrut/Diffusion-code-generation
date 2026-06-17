def get_nested_value(data: dict, *keys) -> any:
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                print(f"Key '{key}' not found at the expected path.")
                return None
        elif isinstance(key, int) and hasattr(data, '__getitem__'):
            pass 
        else:
            raise TypeError("All keys must be strings or integers compatible with dictionary indexing.")
    if current is None:
        print(f"Value at path {keys} is null/None.")
    return current
if __name__ == '__main__':
    hierarchical_data = {
        "user": {
            "id": 101,
            "profile": {
                "name": "Alice Smith",
                "age": 30,
                "hobbies": ["reading", "coding"]
            },
            "address": None                                                                                      
        },
        "company": {
            "name": "TechCorp Inc.",
            "location": {"city": "New York", "country": "USA"}
        }
    }
    user_name = get_nested_value(hierarchical_data, "user", "profile", "name")
    company_loc_city = get_nested_value(hierarchical_data, "company", "location", "city")
    print(f"Retrieved User Name: {user_name}")
    print(f"Retrieved City: {company_loc_city}")
    result_missing = get_nested_value(hierarchical_data, "nonexistent", "path")
    if __name__ == '__main__':
        print(f"Result for missing key attempt: {result_missing}")