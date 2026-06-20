def safe_divide(x, y):
    if y == 0:
        return 'Division by zero'
    return x / y

if __name__ == '__main__':
    dividend = 150.75
    divisor = 3.0
    result = safe_divide(dividend, divisor)
    print(result)