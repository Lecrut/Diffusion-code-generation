def safe_divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

if __name__ == '__main__':
    try:
        result = safe_divide(10, 2)
        print(result)
    except ValueError as e:
        print(e)