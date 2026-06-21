import re
LOGICAL_OPERATORS = {'and', 'or', 'not'}

def parse_and_evaluate(text1, text2):
    conditions1 = re.findall('if\\s+(.*?):\\s*(.*)', text1, re.DOTALL)
    conditions2 = re.findall('if\\s+(.*?):\\s*(.*)', text2, re.DOTALL)
    all_variables = set()
    for cond in conditions1 + conditions2:
        match = re.findall('[A-Za-z_]\\w*', cond[0])
        all_variables.update(match)
    all_variables.update(LOGICAL_OPERATORS)
    variable_truths = {var: None for var in all_variables}

    def eval_condition(condition, truths):
        try:
            return eval(condition, {'__builtins__': None}, truths)
        except Exception as e:
            print(f"Error evaluating condition '{condition}': {e}")
            return False
    for assignment_tuple in product([False, True], repeat=len(variable_truths)):
        variable_assignments = dict(zip(variable_truths.keys(), assignment_tuple))
        truths1 = eval_condition(conditions1[0][0].strip(), variable_assignments)
        truths2 = eval_condition(conditions2[0][0].strip(), variable_assignments)
        if truths1 != truths2:
            return True
    return False
if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10 and z > 20: print('B')"
    sample_string_3 = "if a > 10 and a < 5: print('C')"
    sample_string_4 = "if x > 5 and not (x > 5): print('D')"
    sample_string_5 = "if p or q: print('E')"
    print(parse_and_evaluate(sample_string_1, sample_string_2))
    print(parse_and_evaluate(sample_string_3, sample_string_4))
    print(parse_and_evaluate(sample_string_5, sample_string_1))