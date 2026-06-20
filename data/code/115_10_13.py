def divide_numbers(dividend, divisor):
    if divisor == 0:
        return "Cannot divide by zero"
    return dividend / divisor

if __name__ == '__main__':
    result = divide_numbers(20.5, 4.2)
    print(result)