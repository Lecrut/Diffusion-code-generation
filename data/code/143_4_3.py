import re
from itertools import product
def parse_and_evaluate(text):
    statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
    conditions = []
    for _, condition_str in statements:
        conditions.append(condition_str.strip())
    if not conditions:
        return True
    all_variables = set()
    for cond in conditions:
        match = re.findall(r'[A-Za-z_]\w*', cond)
        all_variables.update(match)
    if not all_variables:
        return True
    variable_list = sorted(list(all_variables))
    num_vars = len(variable_list)
    for assignment_tuple in product([False, True], repeat=num_vars):
        assignment = dict(zip(variable_list, assignment_tuple))
        all_true = True
        for cond_str in conditions:
            try:
                if not eval(cond_str, {}, assignment):
                    all_true = False
                    break
            except Exception:
                all_true = False
                break
        if all_true:
            return True
    return False
if __name__ == '__main__':
    sample_text_1 = "if A > 5: print('A is large')\nif B < 10: print('B is small')"
    sample_text_2 = "if X == True: print('X is true')\nif Y == False: print('Y is false')"
    sample_text_3 = "if A > 10 and B < 5: print('Both are true')"
    sample_text_4 = "if A > 10: print('A is large')"
    print(f"Test 1 (A>5, B<10): {parse_and_evaluate(sample_text_1)}")
    print(f"Test 2 (X==True, Y==False): {parse_and_evaluate(sample_text_2)}")
    print(f"Test 3 (A>10 and B<5): {parse_and_evaluate(sample_text_3)}")
    print(f"Test 4 (A>10): {parse_and_evaluate(sample_text_4)}")