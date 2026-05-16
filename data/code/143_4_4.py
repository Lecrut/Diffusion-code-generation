import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        conditions.append(condition_str.strip())
    if not conditions:
        return True
    num_conditions = len(conditions)
    possible_truth_assignments = list(product([True, False], repeat=num_conditions))
    for assignment in possible_truth_assignments:
        is_simultaneously_true = True
        for i in range(num_conditions):
            pass
        return True
    return False
if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')\nif y < 10: print('B')"
    sample_string_2 = "if a and b: print('C')\nif not a: print('D')"
    sample_string_3 = "if x > 5: print('A')\nif x <= 4: print('B')"
    sample_string_4 = "if x > 5: print('A')\nif x <= 4: print('B')"
    print(f"Test 1: {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2: {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3: {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4: {parse_and_evaluate(sample_string_4)}")