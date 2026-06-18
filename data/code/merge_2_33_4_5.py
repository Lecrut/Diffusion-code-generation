import hashlib
def validate_name(name: str) -> bool:
    authorized_names = {
        "alice",
        "bob",
        "charlie"
    }
    if not isinstance(name, str):
        return False
    normalized_name = name.lower().strip()
    for auth_name in authorized_names:
        if hash(normalized_name) == hash(auth_name):
            return True
    return False
if __name__ == '__main__':
    test_cases = [
        "Alice",
        "bob123",
        "charlie"
    ]
    for case in test_cases:
        result = validate_name(case)
        print(f"{case}: {result}")