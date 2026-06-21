def evaluate_expression(expression):
    cleaned = expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
    cleaned = cleaned.replace('True', 'True').replace('False', 'False')
    try:
        result = eval(cleaned)
        return result
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}") from e

if __name__ == '__main__':
    print(evaluate_expression("True AND False OR True"))
    print(evaluate_expression("NOT True AND False"))
    print(evaluate_expression("True OR False AND False"))
    print(evaluate_expression("NOT (True AND False)"))