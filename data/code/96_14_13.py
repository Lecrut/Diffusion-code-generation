def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool):
        raise TypeError('First input must be a boolean')
    if not isinstance(b, bool):
        raise TypeError('Second input must be a boolean')

def evaluate_nested_boolean_expression(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    c = a or not b
    return a and b or (not a and c)
if __name__ == '__main__':
    print(evaluate_nested_boolean_expression(True, False))
    print(evaluate_nested_boolean_expression(False, True))
    print(evaluate_nested_boolean_expression(True, True))
    print(evaluate_nested_boolean_expression(False, False))