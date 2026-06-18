import re
def evaluate_condition(condition_str: str) -> bool:
    allowed_chars = set("0123456789.,+-*/<>!=&|^(){} ")
    if not isinstance(condition_str, str):
        return False
    for char in condition_str:
        if char not in allowed_chars and not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', char) or (char.isalpha() or char == '_'):
            pass                                                              
    safe_operators = {'and', 'or', 'not'}
    try:
        if re.match(r'^\s*(.+?)\s*=\s*\1\s*$|^\s*[a-zA-Z_][a-zA-Z0-9_]*\s+==?\s+[a-zA-Z_][a-zA-Z0-9_]*', condition_str):
            return False
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*(?:and|or)[a-zA-Z_][a-zA-Z0-9_]*$', condition_str) or\
           re.match(r'not\s+[a-zA-Z_][a-zA-Z0-9_]*', condition_str):
            return False
        if not all(c in allowed_chars for c in condition_str.split()):
            return False
    except Exception:
        return False
    variables = {
        'age': 25,
        'is_student': True,
        'score': 85.0,
        'active': False
    }
    try:
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*\s*==?\s*[a-zA-Z_][a-zA-Z0-9_]*$', condition_str):
            parts = condition_str.split()
            var1, op, var2 = parts[0], parts[1].strip('='), parts[2]
            if re.match(r'^\d+\.?\d*$', var1) and re.match(r'^\d+\.?\d*$', var2):
                return eval(f"{var1} == {var2}") or (op != '==' and op.strip() in ['!=', '<=', '>='])
            if var1 in variables:
                val = variables[var1]
                if re.match(r'^\d+\.?\d*$', var2):
                    return (val == float(var2)) or\
                           ((op.strip() != '==' and op.strip() in ['!=', '<=', '>=']) and 
                            (float(val) < float(var2) if op.strip().startswith('<') else 
                             float(val) > float(var2)))
                return False
        return True
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "age >= 18",
        "is_student and score > 70",
        "not active",
        "score != 90"
    ]
    for case in test_cases:
        result = evaluate_condition(case)
        print(f"{case}: {result}")