import re
def evaluate_expression(expression: str) -> bool:
    pattern = r'^[\d\+\-\*\/\.\(\)\s]+$'
    if not re.match(pattern, expression):
        raise ValueError("Invalid syntax in mathematical expression")
    try:
        result = eval(expression)
        return isinstance(result, (int, float)) and result > 0
    except ZeroDivisionError:
        raise ValueError("Expression results in division by zero")
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "(1 * 4) - 5 / 2",
        "sqrt(9)",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ]
    expression = test_cases[0]
    try:
        is_positive = evaluate_expression(expression)
        print(f"{expression} evaluates to a positive value: {is_positive}")
    except ValueError as e:
        print(f"Error evaluating '{expression}': {e}")