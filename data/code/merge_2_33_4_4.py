import re
def validate_name(name: str) -> bool:
    authorized_names = ["alice", "bob", "charlie"]
    if not isinstance(name, str):
        return False
    normalized_input = name.lower().strip()
    for entry in authorized_names:
        if normalized_input == entry or re.match(rf"^{re.escape(entry)}$", normalized_input):
            return True
    return False
if __name__ == '__main__':
    test_cases = ["Alice", "bob123", "", "charlie"]
    for case in test_cases:
        result = validate_name(case)
        print(f"{case!r}: {result}")