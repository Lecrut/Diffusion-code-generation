import operator

def evaluate_conditions(conditions):
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    operators = {'NOT': operator.not_, 'AND': operator.and_, 'OR': operator.or_}

    def apply_operator(op, stack):
        right = stack.pop()
        left = stack.pop()
        if op == 'NOT':
            stack.append(operators[op](right))
        else:
            stack.append(operators[op](left, right))

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    def evaluate(expression):
        tokens = expression.split()
        stack_operators = []
        stack_values = []
        for token in tokens:
            if token.isdigit():
                stack_values.append(int(token))
            elif token == '(':
                stack_operators.append(token)
            elif token == ')':
                while stack_operators[-1] != '(':
                    apply_operator(stack_operators.pop(), stack_values)
                stack_operators.pop()
            else:
                while stack_operators and stack_operators[-1] != '(' and greater_precedence(stack_operators[-1], token):
                    apply_operator(stack_operators.pop(), stack_values)
                stack_operators.append(token)
        while stack_operators:
            apply_operator(stack_operators.pop(), stack_values)
        return stack_values[0]
    results = [evaluate(condition) for condition in conditions]
    return all(results)
if __name__ == '__main__':
    sample_conditions = ['1 AND 1', '0 OR 1', 'NOT 0']
    print(evaluate_conditions(sample_conditions))