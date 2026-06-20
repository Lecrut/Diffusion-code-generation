def safe_divide(dividend, divisor):
    if divisor == 0:
        return None
    else:
        return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10.0, 2.0)
    print(result)
    result = safe_divide(5.0, 0.0)
    print(result)