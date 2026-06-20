def add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        raise TypeError("Invalid input: Both arguments must be convertible to integers.")

if __name__ == '__main__':
    print(add(5, 10))
    print(add("5", "10"))