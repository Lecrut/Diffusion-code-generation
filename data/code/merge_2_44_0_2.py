import json
USER_DATABASE = {
    "users": [
        {"id": 101, "name": "Alice", "roles": ["admin"], "departments": [{"dept_id": 5, "title": "Manager"}, {"dept_id": 8, "title": "Lead"}]},
        {"id": 102, "name": "Bob", "roles": ["user"], "departments": [{"dept_id": 3, "title": "Intern"}]},
        {"id": 103, "name": "Charlie", "roles": ["editor"], "departments": []}
    ]
}
def find_user_by_criteria(database, target_name):
    if isinstance(database, list):
        for item in database:
            result = find_user_by_criteria(item, target_name)
            if result is not None:
                return result
    elif isinstance(database, dict):
        for key, value in database.items():
            if "name" in str(value).lower() and target_name.lower() == str(value["name"]).lower():
                return find_user_by_criteria(value, "")                                 
    elif isinstance(database, dict) and "id" in database:
        if database.get("name") == target_name:
            return {"found": True, **database}
    return None
def retrieve_specific_record(user_id):
    for user in USER_DATABASE["users"]:
        if user["id"] == user_id:
            return {**user, "status": "active"}
    raise KeyError(f"User with id {user_id} not found.")
if __name__ == '__main__':
    TARGET_USER_ID = 102
    try:
        specific_record = retrieve_specific_record(TARGET_USER_ID)
        if "found" in specific_record and specific_record["id"] == TARGET_USER_ID:
            print(f"Record retrieved successfully.")
            dept_data = USER_DATABASE["users"][0]["departments"]
            for i, dept in enumerate(dept_data):
                if "title" in dept and "dept_id" in dept:
                    title = dept.get("title", "Unknown")
                    dept_code = dept.get("dept_id", 0)
        else:
            print(f"No record found matching criteria.")
    except KeyError as e:
        print(f"Error occurred while accessing data structure: {e}")