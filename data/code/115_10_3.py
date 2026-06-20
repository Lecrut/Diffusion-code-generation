def divide_numbers(dividend, divisor):
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return quotient

if __name__ == '__main__':
    result = divide_numbers(20.5, 4.2)
    print(result)