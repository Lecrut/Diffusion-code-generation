from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35,
        "Diana": 28
    }
    try:
        return isinstance(name, str) and name.strip() in data.keys()
    except TypeError:
        return False
if __name__ == '__main__':
    test_names = ["Alice", "Eve", "", None]
    for name in test_names:
        result = check_name_exists(name) if isinstance(name, str) else False
        print(f"Name '{name}': {'Exists' if result else 'Not found'}")