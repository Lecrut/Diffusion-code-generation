def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)
    result = safe_divide(5, 0)
    print(result)