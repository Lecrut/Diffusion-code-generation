def get_nested_value(data: dict, *keys) -> any:
    current_obj = data
    for key in keys:
        if not isinstance(current_obj, dict):
            return None
        try:
            current_obj = current_obj[key]
        except KeyError:
            return None
    return current_obj
def get_nested_value_safe(data: dict, *keys, default=None) -> any:
    try:
        for key in keys:
            if not isinstance(data, dict):
                return default
            data = data[key]
        return data
    except Exception:                                                
        return default
def main():
    hierarchy = {
        "user": {
            "id": 101,
            "name": "Alice",
            "roles": ["admin", "editor"]
        },
        "project": {
            "title": "Alpha",
            "status": "active"
        }
    }
    user_name = get_nested_value(hierarchy, "user", "name")
    non_existent_role = get_nested_value(hierarchy, "user", "nonexistent_key")
    project_status_safe = get_nested_value_safe(
        hierarchy, 
        "project", 
        "title", 
        "unknown_project"
    )
    print(f"User Name: {user_name}")
    print(f"Non-existent Role (Safe): {non_existent_role}")
    budget = get_nested_value_safe(hierarchy, "project", "budget")
    if __name__ == '__main__':
        main()