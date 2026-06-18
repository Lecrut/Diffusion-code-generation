def find_element_by_key(data: dict, target_key):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    return data.get(target_key)
def find_elements_matching_value(data: dict, target_value):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    matches = []
    for key in data:
        if data[key] == target_value:
            matches.append((key, data[key]))
    return matches
if __name__ == '__main__':
    sample_data = {
        "user_id": 1024,
        "username": "john_doe",
        "email": "john@example.com",
        "role": "admin"
    }
    user_id_value = find_element_by_key(sample_data, "user_id")
    admin_users = find_elements_matching_value(sample_data, "admin")
    print(f"User ID: {user_id_value}")
    if admin_users:
        for key, val in admin_users:
            print(f"Key '{key}' has value '{val}'")