import re
def validate_name(name: str) -> bool:
    authorized_names = ["alice", "bob", "charlie"]
    if not isinstance(name, str):
        return False
    for entry in authorized_names:
        if name.lower() == entry or re.match(rf"^{entry}$", name, re.IGNORECASE):
            return True
    return False
if __name__ == '__main__':
    test_cases = ["Alice", "bob123", "", None]
    for case in test_cases:
        result = validate_name(case) if isinstance(case, str) else False
        print(f"{case!r}: {result}")