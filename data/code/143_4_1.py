import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        match = re.match(r"if\s+(.*?):\s*(.*)", text)
        if match:
            condition = match.group(2).strip()
            conditions.append(condition)
    if not conditions:
        return True
    return True
if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10: print('B')"
    sample_string_3 = "if x > 10 and y < 5: print('C')"
    sample_string_4 = "if x > 10 and x < 5: print('D')"
    print(f"Test 1: {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2: {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3: {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4: {parse_and_evaluate(sample_string_4)}")