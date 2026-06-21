def check_contradictions(statement1: str, statement2: str) -> bool:

    def evaluate_condition(condition: str) -> bool:
        exec(f'return {condition}')
    conditions = [statement1.split('if')[1].strip() if 'if' in statement1 else None, statement2.split('if')[1].strip() if 'if' in statement2 else None]
    if not all(conditions):
        return False
    condition1, condition2 = conditions
    variables = set(re.findall('[A-Za-z_]\\w*', condition1 + condition2))
    for assignment in product([False, True], repeat=len(variables)):
        assignments = dict(zip(variables, assignment))
        if not (evaluate_condition(condition1.format(**assignments)) and evaluate_condition(condition2.format(**assignments))):
            return False
    return True
if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10 and z > 20: print('B')"
    print(check_contradictions(sample_string_1, sample_string_2))
    sample_string_3 = "if a > 10 and a < 5: print('C')"
    sample_string_4 = "if x > 5 and not (x > 5): print('D')"
    print(check_contradictions(sample_string_3, sample_string_4))