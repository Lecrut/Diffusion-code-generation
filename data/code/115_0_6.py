def safe_divide(dividend, divisor):
    if divisor == 0:
        return None
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)
    result = safe_divide(5, 0)
    print(result)