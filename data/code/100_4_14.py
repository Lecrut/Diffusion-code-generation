def is_greater(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both arguments must be integers")
    return x > y

if __name__ == '__main__':
    result1 = is_greater(5, 3)
    result2 = is_greater(2, 4)
    print(result1)
    print(result2)