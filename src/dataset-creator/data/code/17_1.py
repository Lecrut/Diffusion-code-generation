import sys
def validate_items(data_structure: list | set | dict) -> bool:
    required_values = {"apple", "banana"}
    if data_structure is None:
        raise ValueError("Data structure cannot be None")
    try:
        if isinstance(data_structure, (list, tuple)):
            for item in data_structure:
                if not isinstance(item, str):
                    continue
                if item not in required_values:
                    return False
            missing = required_values - set(data_structure)
            if len(missing) > 0:
                raise ValueError(f"Missing items from list: {missing}")
        elif isinstance(data_structure, dict):
            for key in data_structure.keys():
                if not isinstance(key, str):
                    continue
                if key not in required_values:
                    return False
            missing = required_values - set(data_structure.keys())
            if len(missing) > 0:
                raise ValueError(f"Missing keys from dict: {missing}")
        elif isinstance(data_structure, (set)):
            for item in data_structure:
                if not isinstance(item, str):
                    continue
                if item not in required_values:
                    return False
            missing = required_values - set(data_structure)
            if len(missing) > 0:
                raise ValueError(f"Missing items from set: {missing}")
        else:
            raise TypeError("Unsupported data structure type")
    except Exception as e:
        print(f"Validation error occurred: {e}", file=sys.stderr)
        return False
    return True
if __name__ == '__main__':
    sample_list = ["apple", "orange"]
    sample_set = {"banana", "cherry"}
    sample_dict = {"mango": 1, "grape": 2}
    results = {
        "list": validate_items(sample_list),
        "set": validate_items(sample_set),
        "dict": validate_items(sample_dict)
    }
    print("Validation Results:", results)