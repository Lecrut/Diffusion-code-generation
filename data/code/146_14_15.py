def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return result

if __name__ == '__main__':
    print(divide_numbers(10, 2))
    print(divide_numbers(5, 0))