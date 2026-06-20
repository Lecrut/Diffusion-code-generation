def safe_divide(dividend, divisor):
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return quotient

if __name__ == '__main__':
    num1 = 20.5
    num2 = 4.2
    result = safe_divide(num1, num2)
    print(result)