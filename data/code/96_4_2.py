def evaluate_expression(expression):
    if len(expression) == 1:
        return expression[0]
    else:
        left = evaluate_expression(expression[0])
        right = evaluate_expression(expression[1])
        operator = expression[2]
        result = None
        if operator == 'and':
            result = left and right
        elif operator == 'or':
            result = left or right
        elif operator == 'not':
            result = not left
        elif operator == 'xor':
            result = left ^ right
        else:
            raise ValueError("Unknown operator")
        return result
if __name__ == '__main__':
    expression = [['A', 'and', ['B', 'or', ['C', 'not', 'D']]]]
    result = evaluate_expression(expression)
    print(result)