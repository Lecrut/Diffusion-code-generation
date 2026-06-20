def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

if __name__ == '__main__':
    result = divide_numbers(20.5, 4.2)
    print(result)