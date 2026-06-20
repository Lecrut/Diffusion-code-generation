def evaluate_boolean_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def validate_expression(expression):
    if not expression:
        return False, "Expression is empty"
    if not expression.replace(" ", "").isalnum() and not all(c in "+-*/()" for c in expression if c != " "):
        return False, "Invalid characters found"
    return True, ""

def main():
    sample_expressions = [
        "(2 + 3) * 4 > 15",
        "5 + 6 / 2 - 1 == 7",
        "10 / 2 + 5 * 3 < 20",
        "8 - 2 * 3 + 4 != 8"
    ]
    
    for expr in sample_expressions:
        valid, error = validate_expression(expr)
        if not valid:
            print(f"Invalid expression: {error}")
            continue
        result = evaluate_boolean_expression(expr)
        print(f"{expr} evaluates to: {result}")

if __name__ == '__main__':
    main()