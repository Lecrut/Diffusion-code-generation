from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data: Dict[str, Any] = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35,
    }
    return name in data
if __name__ == '__main__':
    test_names = ["Alice", "Diana", "Ethan"]
    for current_name in test_names:
        result = check_name_exists(current_name)
        print(f"Name '{current_name}' exists: {result}")