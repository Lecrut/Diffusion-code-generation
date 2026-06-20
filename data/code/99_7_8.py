def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

if __name__ == '__main__':
    result = evaluate_boolean_expression("2 + 3 > 5 and not False")
    print(result)