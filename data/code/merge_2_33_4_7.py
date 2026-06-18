import re
def validate_name(name: str) -> bool:
    authorized_names = ["alice", "bob", "charlie"]
    if not isinstance(name, str):
        return False
    for allowed in authorized_names:
        pattern = f"^{allowed}$|{re.escape(allowed)}$"
        if re.match(pattern, name):
            return True
    return False
if __name__ == '__main__':
    test_cases = ["alice", "Bob123", "charlie", "", None]
    for case in test_cases:
        result = validate_name(case)
        print(f"{case!r}: {result}")