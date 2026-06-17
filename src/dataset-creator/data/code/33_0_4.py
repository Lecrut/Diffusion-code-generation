from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35,
        "David": 40,
        "Eve": 28
    }
    try:
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Name must be a non-empty string.")
        return name in data
    except Exception as e:
        print(f"Error checking name: {e}")
        return False
if __name__ == '__main__':
    test_names = ["Alice", "Zoe", "", None, 123]
    for name in test_names:
        result = check_name_exists(name) if isinstance(name, str) else f"Invalid type: {type(name).__name__}"
        print(f"Name '{name}': {'Exists' if (isinstance(name, str) and result) else 'Not found'}")