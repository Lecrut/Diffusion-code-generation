import operator
precedence = {
    '==': 1,
    '!=': 1,
    '>': 2,
    '<': 2,
    '>=': 3,
    '<=': 3,
    '&&': 4,
    '||': 4
}
def evaluate_expression(expression, values):
    tokens = expression.split()
    results = []
    for i in range(0, len(tokens), 2):
        op = tokens[i]
        try:
            left = values[i]
            right = values[i+1]
            if op in precedence:
                if op == '==':
                    result = (left == right)
                elif op == '!=':
                    result = (left != right)
                elif op == '>':
                    result = (left > right)
                elif op == '<':
                    result = (left < right)
                elif op == '>=':
                    result = (left >= right)
                elif op == '<=':
                    result = (left <= right)
                elif op == '&&':
                    result = (left and right)
                elif op == '||':
                    result = (left or right)
                results.append(result)
            else:
                raise ValueError(f"Unknown operator: {op}")
        except IndexError:
            raise ValueError("Malformed expression: missing operands")
        except TypeError:
            raise ValueError(f"Type error during evaluation: {op} {left} {right}")
    return results
if __name__ == '__main__':
    sample_expression = "5 > 3 && 10 == 10 || 2 < 1"
    sample_values = [5, 3, 10, 10, 2, 1]
    print(f"Expression: {sample_expression}")
    print(f"Values: {sample_values}")
    try:
        evaluation_results = evaluate_expression(sample_expression, sample_values)
        print(f"Evaluation Results: {evaluation_results}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    sample_expression_2 = "10 >= 5 && 20 < 15"
    sample_values_2 = [10, 5, 20, 15]
    print(f"Expression: {sample_expression_2}")
    print(f"Values: {sample_values_2}")
    try:
        evaluation_results_2 = evaluate_expression(sample_expression_2, sample_values_2)
        print(f"Evaluation Results: {evaluation_results_2}")
    except ValueError as e:
        print(f"Error: {e}")