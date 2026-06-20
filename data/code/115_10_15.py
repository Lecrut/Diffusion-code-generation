DIVISOR_ZERO = 0

def safe_divide(num1, num2):
    if num2 == DIVISOR_ZERO:
        raise ValueError("Error: Division by zero is not allowed.")
    return num1 / num2

if __name__ == '__main__':
    result = safe_divide(20.5, 4.2)
    print(result)