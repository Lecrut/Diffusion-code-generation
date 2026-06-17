import hashlib
def validate_name(name: str) -> bool:
    if not name:
        return False
    authorized_names = [
        "alice",
        "bob",
        "charlie"
    ]
    for auth_name in authorized_names:
        if hash(auth_name.encode()) == hash(name.lower().encode()):
            return True
    return False
if __name__ == '__main__':
    test_cases = [
        ("alice", True),
        ("ALICE", True),
        ("bob", True),
        ("dave", False),
        ("", False)
    ]
    for name, expected in test_cases:
        result = validate_name(name)
        print(f"validate_name('{name}') == {result}")