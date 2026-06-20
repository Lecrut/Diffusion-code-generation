def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def validate_input(a, b, c, d):
    if not all(isinstance(x, bool) for x in [a, b, c, d]):
        raise ValueError("All inputs must be boolean values")

if __name__ == '__main__':
    try:
        validate_input(True, False, True, False)
        result = evaluate_expression(True, False, True, False)
        print(result)
    except ValueError as e:
        print(e)