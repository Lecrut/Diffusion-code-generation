def evaluate_boolean_conditions(conditions):
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    stack_operands = []
    stack_operators = []

    def apply_operator():
        operator = stack_operators.pop()
        right = stack_operands.pop()
        left = stack_operands.pop()
        if operator == 'NOT':
            stack_operands.append(not right)
        elif operator == 'AND':
            stack_operands.append(left and right)
        elif operator == 'OR':
            stack_operands.append(left or right)
    for char in conditions:
        if char == ' ':
            continue
        elif char.isdigit() or (char == '.' and len(stack_operands) > 0 and stack_operands[-1].isdigit()):
            number = float(char)
            stack_operands.append(number)
        elif char in precedence:
            while stack_operators and precedence[char] <= precedence[stack_operators[-1]]:
                apply_operator()
            stack_operators.append(char)
    while stack_operators:
        apply_operator()
    return stack_operands[0]
if __name__ == '__main__':
    sample_conditions = 'NOT (2 > 1) AND (3 < 4 OR 5 == 5)'
    result = evaluate_boolean_conditions(sample_conditions)
    print(result)