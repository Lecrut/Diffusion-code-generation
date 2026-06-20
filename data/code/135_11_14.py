def evaluate_formula(formula, truth_values):
    stack = []
    for char in formula:
        if char.isalpha():
            stack.append(truth_values[char])
        elif char == '¬':
            stack.append(not stack.pop())
        elif char == '&':
            stack.append(stack.pop() and stack.pop())
        elif char == '|':
            stack.append(stack.pop() or stack.pop())
    return stack[0]

def is_equivalent(formula1, formula2):
    variables = set(filter(str.isalpha, formula1 + formula2))
    truth_values = {var: val for var in variables for val in (True, False)}
    for tv in truth_values.values():
        if evaluate_formula(formula1, truth_values) != evaluate_formula(formula2, truth_values):
            return False
    return True
if __name__ == '__main__':
    formula1 = 'A & B'
    formula2 = 'B & A'
    print(is_equivalent(formula1, formula2))
    formula3 = 'A | B'
    formula4 = 'B | C'
    print(is_equivalent(formula3, formula4))