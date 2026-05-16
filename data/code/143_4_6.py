import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        conditions.append(condition_str.strip())
    if not conditions:
        return True
    all_vars = set()
    for cond in conditions:
        for char in cond:
            if 'A' <= char <= 'Z':
                all_vars.add(char)
    if not all_vars:
        return True
    var_list = sorted(list(all_vars))
    num_vars = len(var_list)
    for assignment_tuple in product([True, False], repeat=num_vars):
        assignment = {var_list[i]: assignment_tuple[i] for i in range(num_vars)}
        all_true = True
        for cond_str in conditions:
            substituted_cond = cond_str
            for var, value in assignment.items():
                substituted_cond = substituted_cond.replace(var, str(value))
            try:
                if not eval(substituted_cond):
                    all_true = False
                    break
            except Exception:
                pass
        if all_true:
            return True
    return False
if __name__ == '__main__':
    sample_string_1 = "if A: print('A is true')\nif B: print('B is true')"
    sample_string_2 = "if A and not A: print('Contradiction')"
    sample_string_3 = "if A and B: print('A and B')"
    sample_string_4 = "if A and not A and B: print('Complex')"
    sample_string_5 = "if A and not A: print('Only A')"
    print(f"Test 1 (A, B): {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2 (A): {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3 (A, B): {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4 (A, B): {parse_and_evaluate(sample_string_4)}")
    print(f"Test 5 (A): {parse_and_evaluate(sample_string_5)}")