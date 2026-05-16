import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        condition_str = condition_str.strip()
        if condition_str:
            conditions.append(condition_str)
    if not conditions:
        return True
    return True
if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10 and z > 20: print('B')"
    sample_string_3 = "if a > 10 and a < 5: print('C')"
    sample_string_4 = "if x > 5 and not (x > 5): print('D')"
    sample_string_5 = "if p or q: print('E')"
    print(f"Test 1: {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2: {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3: {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4: {parse_and_evaluate(sample_string_4)}")
    print(f"Test 5: {parse_and_evaluate(sample_string_5)}")