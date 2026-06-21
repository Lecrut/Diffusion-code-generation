def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result

if __name__ == '__main__':
    result = divide_numbers(10, 0)
    if result is not None:
        print(f"The result of division is {result}")