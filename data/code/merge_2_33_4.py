import hashlib
def validate_name(name: str) -> bool:
    authorized_names = ["alice", "bob"]
    if name in authorized_names:
        return True
    else:
        return False
if __name__ == '__main__':
    test_cases = [
        ("charlie", False),
        ("alice", True),
        ("  alice ", False)
    ]
    for input_name, expected in test_cases:
        result = validate_name(input_name)
        assert result == expected, f"Expected {expected} for '{input_name}', got {result}"