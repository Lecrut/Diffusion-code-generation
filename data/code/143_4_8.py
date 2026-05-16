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
    all_propositions = set()
    for cond in conditions:
        parts = cond.split(' and ')
        for part in parts:
            part = part.strip()
            if part and not part.startswith('(') and not part.endswith(')'):
                all_propositions.add(part)
    if not all_propositions:
        return True
    return True
if __name__ == '__main__':
    sample_string_1 = "if A: print('A is true')\nif B: print('B is true')"
    sample_string_2 = "if A and B: print('A and B are true')"
    sample_string_3 = "if A: print('A is true')\nif not A: print('Not A is true')"
    sample_string_4 = "if A: print('A is true')"
    print(f"Test 1 Result: {parse_and_evaluate(sample_string_1)}")
    print(f"Test 2 Result: {parse_and_evaluate(sample_string_2)}")
    print(f"Test 3 Result: {parse_and_evaluate(sample_string_3)}")
    print(f"Test 4 Result: {parse_and_evaluate(sample_string_4)}")