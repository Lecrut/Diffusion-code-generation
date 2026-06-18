def get_nested_value(data: dict, *keys) -> any:
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                return None
        elif isinstance(key, int) and hasattr(current, '__getitem__'):
            try:
                current = current[key]
            except (IndexError, KeyError):
                return None
        else:
            raise TypeError(f"Unsupported key type or data structure. Expected dict/list access.")
    if not isinstance(current, dict):
        return current                                                 
    return None
def build_sample_dataset() -> dict:
    return {
        "user": {
            "id": 101,
            "name": {"first": "Alice", "last": "Johnson"},
            "contact": {
                "email": "alice@example.com",
                "phone": "+1-555-0199"
            },
            "preferences": ["python", "data_science"]
        }
    }
def main():
    dataset = build_sample_dataset()
    user_id = get_nested_value(dataset, "user", "id")
    missing_email = get_nested_value(dataset, "user", "missing_key")
    first_name = get_nested_value(dataset, "user", "name", "first")
    last_name = get_nested_value(dataset, "user", "name", "last")
    print(f"User ID: {user_id}")
    if missing_email is None:
        print("Email lookup failed (expected behavior for non-existent key).")
    else:
        print(f"Full Email: {missing_email}")                                     
    full_name = f"{first_name} {last_name}"
    print(f"User Name: {full_name}")
if __name__ == '__main__':
    main()