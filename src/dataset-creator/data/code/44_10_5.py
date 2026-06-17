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
            }
        },
        "preferences": {
            "theme": "dark",
            "notifications": True,
            "settings": {"language": "en-US"}
        },
        "metadata": None                                                      
    }
def main():
    dataset = build_sample_dataset()
    first_name = get_nested_value(dataset, "user", "name", "first")
    last_name = get_nested_value(dataset, "user", "name", "last")
    email_address = get_nested_value(dataset, "user", "contact", "email")
    missing_key_result = get_nested_value(dataset, "nonexistent_path", 123)
    print(f"User Name: {first_name} {last_name}")
    print(f"Email Address: {email_address}")
    print(f"Missing Key Result: {missing_key_result}")
if __name__ == '__main__':
    main()