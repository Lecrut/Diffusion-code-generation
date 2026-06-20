def evaluate_boolean_expression(expression):
    def validate(expression):
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        if not expression:
            raise ValueError("Expression cannot be empty")

    validate(expression)
    
    result = eval(expression)
    return result

if __name__ == '__main__':
    sample_expression = "((True and False) or (not True))"
    print(evaluate_boolean_expression(sample_expression))