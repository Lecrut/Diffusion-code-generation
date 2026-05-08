def safe_eval_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"
expression1 = "10 + 5 * 2"
expression2 = "(10 + 5) * 2"
expression3 = "10 + 5 * 2 - 1"
expression4 = "10 + 5 * (2 - 1)"
print(f"Evaluating '{expression1}': {safe_eval_expression(expression1)}")
print(f"Evaluating '{expression2}': {safe_eval_expression(expression2)}")
print(f"Evaluating '{expression3}': {safe_eval_expression(expression3)}")
print(f"Evaluating '{expression4}': {safe_eval_expression(expression4)}")
print("\n--- Explanation of Precedence ---")
print("Python's eval() respects standard mathematical operator precedence rules.")
print("1. Multiplication (*) and Division (/) have higher precedence than Addition (+) and Subtraction (-).")
print("2. Parentheses () override standard precedence, forcing the operations inside them to be evaluated first.")
print("\nExample Breakdown:")
print(f"'{expression1}' (10 + 5 * 2): Multiplication (5 * 2 = 10) is performed before addition. Result: 10 + 10 = 20.")
print(f"'{expression2}' ((10 + 5) * 2): Parentheses force the addition (10 + 5 = 15) to happen first. Then multiplication (15 * 2 = 30).")
print(f"'{expression3}' (10 + 5 * 2 - 1): Multiplication (5 * 2 = 10) is done first, then addition and subtraction from left to right. (10 + 10 - 1 = 19).")
print(f"'{expression4}' (10 + 5 * (2 - 1)): Parentheses force (2 - 1 = 1) first. Then multiplication (5 * 1 = 5). Finally, addition (10 + 5 = 15).")
if __name__ == '__main__':
    pass