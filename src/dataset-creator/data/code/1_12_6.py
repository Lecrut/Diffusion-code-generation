import re
def evaluate_condition(condition_str: str) -> bool:
    try:
        allowed_vars = {'age': 25, 'is_student': True, 'score': 80}
        safe_expr = re.sub(r'\b(age|is_student|score)\b', lambda m: str(allowed_vars[m.group()]), condition_str)
        return eval(safe_expr, {"__builtins__": {}}, {})
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "age > 18 and is_student",
        "score >= 90 or age < 25",
        "!is_student"
    ]
    for case in test_cases:
        result = evaluate_condition(case)
        print(f"{case} -> {result}")