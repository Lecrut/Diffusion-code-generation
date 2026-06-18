import re
def validate_authorized_name(name: str) -> bool:
    authorized_names = ["alice", "bob", "charlie"]
    if not isinstance(name, str):
        return False
    for entry in authorized_names:
        if name.lower() == entry or re.match(rf"^{re.escape(entry)}$", name, re.IGNORECASE):
            return True
    return False
if __name__ == '__main__':
    test_cases = ["alice", "ALICE", "bob123", "", None]
    for case in test_cases:
        result = validate_authorized_name(case) if isinstance(case, str) else False
        print(f"Input: {case!r} -> Output: {result}")