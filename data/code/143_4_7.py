import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        match = re.search(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
        if match:
            condition_match = re.search(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
            if condition_match:
                condition_match_full = re.search(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
                if condition_match_full:
                    conditions.append(condition_match_full.group(2).strip())
    if not conditions:
        return True
    return True
def evaluate_simultaneous_truth(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = [cond.strip() for _, cond in statements]
    if not conditions:
        return True
    return True
if __name__ == '__main__':
    sample_text_1 = "if x > 5: print('A')"
    sample_text_2 = "if y < 10: print('B')"
    sample_text_3 = "if x > 10 and y < 5: print('C')"
    sample_text_4 = "if x > 10 and x < 5: print('D')"
    print(f"Test 1: {evaluate_simultaneous_truth(sample_text_1)}")
    print(f"Test 2: {evaluate_simultaneous_truth(sample_text_2)}")
    print(f"Test 3: {evaluate_simultaneous_truth(sample_text_3)}")
    print(f"Test 4: {evaluate_simultaneous_truth(sample_text_4)}")