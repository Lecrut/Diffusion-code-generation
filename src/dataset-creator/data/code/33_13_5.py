from collections import defaultdict, deque
def check_existence(target):
    data_structures = {
        "list": [10, 20, 30],
        "set": {"apple", "banana"},
        "dict_key_check": {"key_a": "value_1", "key_b": "value_2"},
        "tuple": (5.5, 6.6),
        "deque": deque(["x", "y"]),
    }
    results = {}
    if target in data_structures["list"]:
        results["list"] = True
    if target in data_structures["set"]:
        results["set"] = True
    for key, value in data_structures["dict_key_check"].items():
        if str(target) == str(key):
            results[f"dict_{key}"] = True
    if target in data_structures["tuple"]:
        results["tuple"] = True
    if target in data_structures["deque"]:
        results["deque"] = True
    return results
if __name__ == '__main__':
    test_values = ["20", "apple", "key_a", 5.5, "nonexistent"]
    for val in test_values:
        print(f"Checking value: {val}")
        found_in = check_existence(val)
        if any(found_in.values()):
            present_structures = [k for k, v in found_in.items() if v]
            print(f"Found in: {present_structures}")
        else:
            print("Not found in any structure")