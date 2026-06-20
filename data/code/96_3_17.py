def evaluate_boolean_expression(expression):
    operators = {
        'and': lambda x, y: x and y,
        'or': lambda x, y: x or y
    }

    def solve(sub_expression):
        if isinstance(sub_expression, list) and len(sub_expression) == 3:
            left = solve(sub_expression[0])
            operator = sub_expression[1]
            right = solve(sub_expression[2])
            return operators.get(operator, lambda x, y: False)(left, right)
        else:
            return bool(sub_expression)

    return solve(expression)

if __name__ == '__main__':
    sample_expression = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = evaluate_boolean_expression(sample_expression)
    print(result)