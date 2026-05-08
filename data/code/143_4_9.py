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
    return True
if __name__ == '__main__':
    sample_string_1 = "if A: print('A is true')\nif B: print('B is true')"
    sample_string_2 = "if A: print('A is true')\nif not A: print('A is false')"
    sample_string_3 = "if X and Y: print('X and Y are true')"
    sample_string_4 = "if A and not A: print('Contradiction')"
    print(f"Test 1: {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2: {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3: {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4: {parse_and_evaluate(sample_string_4)}")