import json
USER_DATABASE = {
    "users": [
        {"id": 101, "name": "Alice", "address": {"city": "New York", "zip": "10001"}, "hobbies": ["reading", "coding"]},
        {"id": 102, "name": "Bob", "address": {"city": "Los Angeles", "zip": "90001"}, "hobbies": ["gaming"]}
    ]
}
def retrieve_user_by_id(user_database, target_id):
    for item in user_database.get("users", []):
        if isinstance(item, dict) and item.get("id") == target_id:
            return item
    for key, value in user_database.items():
        if isinstance(value, list):
            for sub_item in value:
                if isinstance(sub_item, dict) and "id" in sub_item and sub_item["id"] == target_id:
                    return sub_item
        elif isinstance(value, dict):
            result = retrieve_user_by_id(value, target_id)
            if result is not None:
                return result
    raise ValueError(f"No user found with ID {target_id}")
def get_nested_value(data, path):
    try:
        current = data
        for key in path:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current
    except (KeyError, TypeError):
        return None
if __name__ == '__main__':
    TARGET_USER_ID = 102
    try:
        user_record = retrieve_user_by_id(USER_DATABASE, TARGET_USER_ID)
        if user_record is not None:
            print(f"Found User ID {TARGET_USER_ID}:")
            city_zip_path = ["address", "city"]                                 
            city_value = get_nested_value(user_record, city_zip_path)
            zip_code = get_nested_value(user_record, ["address", "zip"])
            print(f"City: {city_value}")
            print(f"Zip Code: {zip_code}")
        else:
            print("User record not found.")
    except ValueError as ve:
        print(str(ve))