def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

if __name__ == '__main__':
    num1 = 10
    num2 = 0
    division_result = divide_numbers(num1, num2)
    if division_result is not None:
        print(f"The result of the division is: {division_result}")