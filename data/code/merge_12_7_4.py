def safe_subtract(a, b):
    if b > a:
        return a - b
    else:
        return a - b
if __name__ == '__main__':
    print(safe_subtract(10, 5))
    print(safe_subtract(5, 10))
    print(safe_subtract(7, 7))
    print(safe_subtract(3, 8))
    print(safe_subtract(20.5, 10.5))
    print(safe_subtract(4, 12))