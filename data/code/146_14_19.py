def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error during division: {e}")
        return None
    else:
        return result

if __name__ == '__main__':
    a = 10
    b = 0
    result = divide_numbers(a, b)
    if result is not None:
        print(result)