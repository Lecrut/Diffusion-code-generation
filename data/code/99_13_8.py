def is_valid_operator(operator):
    return operator in {'and', 'or'}

def evaluate_conditions(cond1, cond2, operator):
    if not is_valid_operator(operator):
        raise ValueError('Invalid operator')
    return (cond1 and cond2) if operator == 'and' else (cond1 or cond2)

if __name__ == '__main__':
    a = True
    b = False
    operator = 'or'
    result = evaluate_conditions(a, b, operator)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Operator: {operator}")
    print(f"Result of ({a} and {b}) if '{operator}' else ({a} or {b}): {result}")