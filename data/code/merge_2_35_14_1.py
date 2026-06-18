from typing import Any, Dict, Tuple
def find_by_value(data: Dict[Any, Any], target: Any) -> Tuple[bool, Any]:
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    for key in data:
        value = data[key]
        if value == target:
            return True, (key, value)
    return False, None
def check_key_exists(data: Dict[Any, Any], search_key: Any) -> bool:
    return search_key in data
if __name__ == '__main__':
    database_records: Dict[str, int] = {
        "user_001": 85,
        "user_002": 92,
        "user_003": 78,
        "admin_user": 100
    }
    target_score = 92
    found_key_value, result_tuple = find_by_value(database_records, target_score)
    if found_key_value and isinstance(result_tuple, tuple):
        print(f"Value {target_score} found at key: {result_tuple[0]}")
    else:
        print(f"Value {target_score} not found.")
    critical_key = "admin_user"
    is_present = check_key_exists(database_records, critical_key)
    if is_present:
        value_at_critical_key = database_records[critical_key]
        print(f"Key '{critical_key}' exists with value {value_at_critical_key}")
    else:
        print(f"Key '{critical_key}' does not exist.")
    phantom_key = "non_existent_user"
    is_phantom_present = check_key_exists(database_records, phantom_key)
    if not is_phantom_present:
        print(f"Key '{phantom_key}' correctly identified as absent.")
    missing_value = -999
    found_missing, result_tuple_2 = find_by_value(database_records, missing_value)
    if not found_missing and isinstance(result_tuple_2, tuple):
        print(f"Value {missing_value} correctly identified as absent.")