def safe_divide(dividend, divisor):
    if divisor == 0:
        return 'Division by zero'
    else:
        return dividend / divisor
if __name__ == '__main__':
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))