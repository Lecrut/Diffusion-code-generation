from typing import Dict, Any
def check_name_exists(names: Dict[str, Any], target_name: str) -> bool:
    return target_name in names.keys()
if __name__ == '__main__':
    sample_data = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    test_names: list[str] = ["Alice", "David", None, "", "Eve"]
    for name in test_names:
        if isinstance(name, str):
            exists = check_name_exists(sample_data, name)
            print(f"Name '{name}' exists: {exists}")
        else:
            print(f"Ignoring invalid type for name: {type(name)}")