def safe_division(dividend, divisor):
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    return dividend / divisor

def perform_division():
    num1 = 20.5
    num2 = 4.2
    result = safe_division(num1, num2)
    print(result)

if __name__ == '__main__':
    perform_division()