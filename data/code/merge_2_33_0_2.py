from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35,
    }
    try:
        return isinstance(data.get(name), int) and len(name.strip()) > 0
    except Exception:
        return False
if __name__ == '__main__':
    test_names = ["Alice", "", "Bob", None]
    for name in test_names:
        if check_name_exists(str(name)):
            print(f"Name '{name}' exists.")
        else:
            print(f"Name '{name}' does not exist or is invalid.")