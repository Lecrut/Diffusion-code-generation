import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        match = re.search(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
        if match:
            condition = match.group(1).strip()
            conditions.append(condition)
    if not conditions:
        return True
    all_variables = set()
    for cond in conditions:
        variables = re.findall(r'[a-zA-Z0-9_]+', cond)
        all_variables.update(variables)
    if not all_variables:
        return True
    for cond in conditions:
        if "and not" in cond or "or" in cond:
            pass
    return True
if __name__ == '__main__':
    sample_string_1 = "if A: print('A is true')\nif B: print('B is true')"
    sample_string_2 = "if A and B: print('A and B are true')"
    sample_string_3 = "if A and not A: print('Contradiction')"
    sample_string_4 = "if X: print('X is true')"
    print(f"Test 1 (A, B): {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2 (A and B): {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3 (A and not A): {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4 (X): {parse_and_evaluate(sample_string_4)}")