def is_greater(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both inputs must be integers")
    return x > y

if __name__ == '__main__':
    result1 = is_greater(5, 3)
    result2 = is_greater(2, 4)
    print(f"Is 5 greater than 3? {result1}")
    print(f"Is 2 greater than 4? {result2}")