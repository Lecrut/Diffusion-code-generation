import operator
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    a = 10
    b = 5
    c = 2
    d = 3
    expression1 = "10 + 5 * 2"
    result1 = calculate_expression(expression1)
    print(f"Expression: {expression1}")
    print(f"Result: {result1}\n")
    expression2 = "(10 + 5) * 2"
    result2 = calculate_expression(expression2)
    print(f"Expression: {expression2}")
    print(f"Result: {result2}\n")
    expression3 = "20 - 10 / 2 * 3 % 4"
    result3 = calculate_expression(expression3)
    print(f"Expression: {expression3}")
    print(f"Result: {result3}\n")
    expression4 = "10 ** 2 + 3 // 4"
    result4 = calculate_expression(expression4)
    print(f"Expression: {expression4}")
    print(f"Result: {result4}\n")
    expression5 = "((a * b) + c) / (d - 1)"
    expression5_evaluated = expression5.replace("a", str(a)).replace("b", str(b)).replace("c", str(c)).replace("d", str(d))
    result5 = calculate_expression(expression5_evaluated)
    print(f"Expression: {expression5}")
    print(f"Result: {result5}\n")
    expression6 = "17 % 5 * 2"
    result6 = calculate_expression(expression6)
    print(f"Expression: {expression6}")
    print(f"Result: {result6}\n")