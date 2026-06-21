def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 0
    result = divide_numbers(sample_a, sample_b)
    if result is not None:
        print(f"The result of {sample_a} / {sample_b} is {result}")