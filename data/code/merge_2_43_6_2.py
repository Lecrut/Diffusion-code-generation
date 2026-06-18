import json
def remove_from_list(data: list, target) -> bool:
    if data is not None and target in data:
        return data.remove(target)
    return False
def remove_key_if_present(dictionary: dict, key) -> bool:
    if isinstance(dictionary, dict):
        if key in dictionary:
            del dictionary[key]
            return True
    return False
def remove_from_dict_nested(data: list | None, target_value=None, match_key=None) -> bool:
    if isinstance(data, dict):
        for key in list(data.keys()):
            if match_key and str(key).lower() == match_key.lower():
                del data[key]
                return True
            elif target_value is not None:
                val = data.get(key)
                remove_from_dict_nested(val, target_value=target_value)
    elif isinstance(data, list):
        for i in range(len(data)):
            item = data[i]
            if match_key and str(item).lower() == match_key.lower():
                del data[i]
                return True
            elif target_value is not None:
                remove_from_dict_nested(item, target_value=target_value)
    return False
def main() -> int | float | None:
    sample_list = [10, "apple", 20.5, "banana"]
    sample_dict = {"fruit": "apple", "number": 10}
    nested_data = [{"id": 1}, {"name": "orange"}]
    remove_from_list(sample_list, "apple")
    print(f"List after removal: {sample_list}")
    remove_key_if_present(sample_dict, "number")
    print(f"Dict after key removal: {sample_dict}")
    nested_data = [{"id": 1}, {"name": "orange"}]
    result_nested = remove_from_dict_nested(nested_data)
    if isinstance(result_nested, bool):
        return float(result_nested) * 2.0 if result_nested else None
if __name__ == '__main__':
    main()