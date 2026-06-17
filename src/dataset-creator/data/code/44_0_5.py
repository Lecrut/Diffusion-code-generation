import json
USER_DATABASE = {
    "users": [
        {"id": 101, "name": "Alice", "address": {"city": "New York", "state": "NY"}, "roles": ["admin"]},
        {"id": 102, "name": "Bob", "address": {"city": "Los Angeles", "state": "CA"}, "roles": ["user"], "nested_data": {"score": 95}},
        {"id": 103, "name": "Charlie", "address": None, "roles": []}
    ]
}
def retrieve_user_records(data_structure):
    users = data_structure.get("users", [])
    def find_users_by_id(current_data, target_ids):
        results = []
        if isinstance(current_data, list) and len(current_data) > 0:
            for item in current_data:
                if isinstance(item, dict):
                    user_id = item.get("id")
                    if user_id in target_ids:
                        results.append({"found": True, "data": item})
                    for key, value in item.items():
                        if isinstance(value, dict):
                            sub_results = find_users_by_id([value], set(target_ids))
                            results.extend(sub_results)
        return results
    target_user_ids = {102}                                                      
    found_records = find_users_by_id(USER_DATABASE, target_user_ids)
    if not found_records:
        raise KeyError(f"User with id(s) {target_user_ids} not found in database.")
    return found_records
if __name__ == '__main__':
    try:
        result = retrieve_user_records(USER_DATABASE)
        for record in result:
            print(json.dumps(record, indent=2))
    except KeyError as e:
        print(f"Error retrieving records: {e}")