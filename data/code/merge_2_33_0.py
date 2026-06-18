from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data = {"Alice": 30, "Bob": 25, "Charlie": 35}
    try:
        return name in data
    except TypeError as e:
        raise ValueError("Name must be a string.") from e
if __name__ == '__main__':
    test_cases = ["Alice", "Diana", "", "123"]
    for candidate in test_cases:
        result = check_name_exists(candidate)
        print(f"Is '{candidate}' found? {result}")