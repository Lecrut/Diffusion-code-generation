import re
def evaluate_condition(user_input: str) -> bool:
    try:
        if not isinstance(user_input, str):
            return False
        conditions = {
            "is_long": len(user_input.strip()) > 10,
            "contains_digit": any(c.isdigit() for c in user_input),
            "has_uppercase": any(c.isupper() for c in user_input),
            "ends_with_letter": re.search(r'[a-zA-Z]$', user_input) is not None,
        }
        return (conditions["is_long"] and conditions["contains_digit"]) or\
               (conditions["has_uppercase"] and conditions["ends_with_letter"])
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "Hello123",
        "abcde",
        "Test99!",
        "short",
        "",
        "Python is great 2024"
    ]
    results = []
    for case in test_cases:
        result = evaluate_condition(case)
        results.append(f'Input: "{case}" -> {result}')
    print("\n".join(results))