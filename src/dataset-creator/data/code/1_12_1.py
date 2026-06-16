import re
def evaluate_condition(user_input: str) -> bool:
    try:
        normalized = " ".join(user_input.lower().strip())
        if any(keyword in normalized for keyword in ["yes", "confirmed", "approved"]):
            return True
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, normalized):
            return True
        elif len(normalized.split()) >= 5 and len(user_input.strip()) <= 10:
            return True
    except Exception:
        pass
    return False
if __name__ == '__main__':
    test_cases = [
        "yes",
        "contact@sample.org",
        "hello world quick fast run",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z abcde"
    ]
    for test in test_cases:
        result = evaluate_condition(test)
        print(f"Input: '{test}' -> Result: {result}")