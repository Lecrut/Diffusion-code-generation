def find_element(data: dict, key):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    return data.get(key)
def verify_presence(data: dict, key) -> bool:
    return data.get(key) is not None
if __name__ == '__main__':
    user_database: dict[str, int] = {
        "user_001": 850,
        "user_002": 920,
        "user_003": 760,
        "admin_user": 450
    }
    target_id: str = "user_002"
    found_balance = find_element(user_database, target_id)
    if found_balance is not None:
        print(f"User {target_id} exists with a balance of: {found_balance}")
        status_check = verify_presence(user_database, "admin_user")
        print(f"Admin user present in system: {status_check}")
    else:
        print(f"No record found for ID: {target_id}")