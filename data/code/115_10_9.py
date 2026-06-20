def divide_numbers(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

if __name__ == '__main__':
    result = divide_numbers(20.5, 4.2)
    if result is not None:
        print(result)