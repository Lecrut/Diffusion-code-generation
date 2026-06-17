from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35,
        "David": 40
    }
    try:
        return name in data
    except TypeError as e:
        raise ValueError(f"Invalid input type. Expected string, got {type(name).__name__}.") from e
if __name__ == '__main__':
    test_names = ["Alice", "Eve", "", None]
    for candidate in test_names:
        try:
            result = check_name_exists(candidate) if isinstance(candidate, str) else False
            print(f"Name '{candidate}': {'Found' if result else 'Not found'}")
        except ValueError as ve:
            print(f"Error checking name {repr(candidate)}: {ve}")