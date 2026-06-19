def is_strictly_greater(a, b):
    try:
        return float(a) > float(b)
    except ValueError:
        return False
if __name__ == '__main__':
    print(is_strictly_greater(10, 5))
    print(is_strictly_greater(3.5, 4.2))
    print(is_strictly_greater('7', '3'))
    print(is_strictly_greater('abc', 1))