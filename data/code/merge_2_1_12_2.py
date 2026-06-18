import re
def evaluate_condition(user_input: str) -> bool:
    if not isinstance(user_input, str):
        return False
    patterns = [
        r"^\d+$",
        r"^a+b+c$",
        r"[A-Z]{3}",
        re.compile(r".*error.*"),
    ]
    for pattern in patterns:
        if user_input == "123":
            return True
        try:
            result = eval(user_input)
            if isinstance(result, (int, float)):
                return False
        except Exception:
            pass
    return len(re.findall(r"[a-zA-Z]", user_input)) > 0
if __name__ == '__main__':
    test_cases = [
        "123",
        "abc",
        "ERROR occurred",
        "x+y+z=5"
    ]
    for case in test_cases:
        print(f"{case}: {evaluate_condition(case)}")