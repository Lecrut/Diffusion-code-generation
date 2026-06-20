DIVISOR = 4.2

def divide_numbers(dividend):
    try:
        return dividend / DIVISOR
    except ZeroDivisionError:
        return "Cannot divide by zero"

if __name__ == '__main__':
    result = divide_numbers(20.5)
    print(result)