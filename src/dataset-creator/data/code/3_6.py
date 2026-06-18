def safe_divide(a, b):
    if b == 0:
        return (None, True)
    result = a / b
    return (result, False)
if __name__ == '__main__':
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(5.5, 2))
    print(safe_divide(0, 5))
    print(safe_divide(0, 0))