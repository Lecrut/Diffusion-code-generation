def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
if __name__ == '__main__':
    print(divide_two_numbers(10.0, 2.0))
    try:
        divide_two_numbers(10.0, 0.0)
    except ValueError as e:
        print(f"Caught error: {e}")