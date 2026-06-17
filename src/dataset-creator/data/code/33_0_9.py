from typing import Dict, Any
def check_name_exists(name: str) -> bool:
    data = {
        "alice": 30,
        "bob": 25,
        "charlie": 31,
    }
    try:
        value = data[name]
        return True
    except KeyError:
        return False
if __name__ == '__main__':
    test_names = ["alice", "david", None, "", "bob"]
    for name in test_names:
        if isinstance(name, str):
            exists = check_name_exists(name)
            print(f"Name '{name}' exists: {exists}")