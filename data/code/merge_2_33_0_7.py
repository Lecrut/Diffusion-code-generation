from typing import Dict, Any, Optional
def check_name_in_dict(
    name: str, 
    data: Dict[str, Any]
) -> bool:
    return name in data
if __name__ == '__main__':
    sample_data = {
        "alice": 30,
        "bob": 25,
        "charlie": 35
    }
    test_names: list[str] = ["dave", "eve", "alice"]
    for name in test_names:
        result = check_name_in_dict(name, sample_data)
        print(f"Name '{name}' exists: {result}")