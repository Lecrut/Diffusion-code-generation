import sys
def safe_nested_access(data: dict) -> tuple[bool, str]:
    try:
        path = data.get("path", "").split("/") if "path" in data else []
        current = data
        for key in path:
            if isinstance(current, dict):
                current = current.get(key)
            elif isinstance(current, list):
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return False, f"Index {key} out of bounds."
            if not isinstance(current, (dict, list)):
                return True, "Value is a primitive type or None."
        result_value = data.get("value", "")
        return True, str(result_value)
    except Exception as e:
        return False, f"Unexpected error occurred during access: {str(e)}"
def generate_nested_data() -> dict:
    data = {}
    user_config = {"name": "TestUser", "path": "/settings/profile/email"}
    email_value = "user@example.com"
    nested_structure = [
        {
            "id": 1,
            "data": {
                "level2_key_1": {"nested_dict_val": "DeepValue"},
                "list_item_a": ["item1", "item2"],
                "list_item_b": [{"sub_list": [[[[["innermost"]]]]]}]
            }
        },
        {
            "id": 2,
            "data": {"level2_key_2": None}
        }
    ]
    data.update({"user_config": user_config})
    data.update({"nested_structure": nested_structure})
    return data
def optimize_access_performance(data: dict) -> list[str]:
    results = []
    for item in data.get("nested_structure", []):
        try:
            if isinstance(item, dict):
                inner_data = item.get("data")
                deep_val = None
                if isinstance(inner_data, dict) and "level2_key_1" in inner_data:
                    lvl2_dict = inner_data["level2_key_1"]
                    if isinstance(lvl2_dict, dict):
                        deep_val = lvl2_dict.get("nested_dict_val")
                safe_list_access = []
                for idx in range(len(item)):
                    try:
                        val = item[idx] if isinstance(item, (list, dict)) else None
                        safe_list_access.append(val)
                    except IndexError:
                        continue
                results.append(f"Processed ID {item.get('id')}: Deep value={deep_val}, List access count={len(safe_list_access)}")
        except Exception as e:
            pass
    return results
def main():
    sample_data = generate_nested_data()
    print("Running Safe Nested Access Patterns...")
    status, message = safe_nested_access(sample_data)
    if not isinstance(status, bool):
        sys.exit(1)
    print(f"Test 1 Status: {status}")
    print(f"Message: {message}\n")
    optimized_results = optimize_access_performance(sample_data)
    for res in optimized_results:
        if isinstance(res, str):
            print(res)
if __name__ == '__main__':
    main()