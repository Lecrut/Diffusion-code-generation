def evaluate_formula(formula, truth_values):
    stack = []
    for char in formula:
        if char == 'T':
            stack.append(True)
        elif char == 'F':
            stack.append(False)
        elif char == '!':
            stack.append(not stack.pop())
        elif char == '&':
            stack.append(stack.pop() and stack.pop())
        elif char == '|':
            stack.append(stack.pop() or stack.pop())
    return stack[0]

def is_equivalent(formula1, formula2):
    variables = set()
    for char in formula1 + formula2:
        if char.isalpha():
            variables.add(char)
    truth_values = {var: [True, False] for var in variables}
    all_combinations = list(product(*truth_values.values()))
    for combination in all_combinations:
        values_dict = dict(zip(truth_values.keys(), combination))
        result1 = evaluate_formula(formula1.replace('T', 'True').replace('F', 'False'), values_dict)
        result2 = evaluate_formula(formula2.replace('T', 'True').replace('F', 'False'), values_dict)
        if result1 != result2:
            return False
    return True
if __name__ == '__main__':
    formula1 = 'A&B'
    formula2 = 'B&A'
    print(is_equivalent(formula1, formula2))
    formula3 = 'A|B'
    formula4 = 'B|A'
    print(is_equivalent(formula3, formula4))
    formula5 = 'A&!B'
    formula6 = '!B&A'
    print(is_equivalent(formula5, formula6))