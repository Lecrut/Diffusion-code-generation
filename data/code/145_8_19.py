import operator
LOGICAL_AND = 'AND'
LOGICAL_OR = 'OR'

def evaluate_predicate(predicate_list):
    for predicate in predicate_list:
        if not predicate():
            return False
    return True

def evaluate_expression(expression, values):
    tokens = expression.split()
    if not tokens:
        raise ValueError('Empty expression')

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == LOGICAL_AND:
            values.append(operator(left, right))
        elif operator == LOGICAL_OR:
            values.append(operator(left, right))

    def greater_than(a, b):
        return a > b

    def less_than(a, b):
        return a < b

    def equals(a, b):
        return a == b
    operators = {LOGICAL_AND: operator.and_, LOGICAL_OR: operator.or_}
    values_map = {f'v{i}': value for i, value in enumerate(values)}
    stack_operators = []
    stack_values = []
    for token in tokens:
        if token in values_map:
            stack_values.append(values_map[token])
        elif token in operators:
            while stack_operators and operators[token] != LOGICAL_OR and (operators[stack_operators[-1]] == LOGICAL_AND):
                apply_operator(stack_operators, stack_values)
            stack_operators.append(token)
        else:
            raise ValueError(f'Invalid token: {token}')
    while stack_operators:
        apply_operator(stack_operators, stack_values)
    return stack_values[0]
if __name__ == '__main__':
    predicates = [lambda: 1 > 0, lambda: 2 < 3, lambda: 4 == 4]
    print(evaluate_predicate(predicates))
    expression = 'v0 AND v1 OR v2'
    values = [1, 2, 4]
    result = evaluate_expression(expression, values)
    print(result)