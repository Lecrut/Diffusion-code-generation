def add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        raise ValueError("Both inputs must be convertible to integers.")

if __name__ == '__main__':
    print(add(5, 10))
    print(add("5", "10"))
    try:
        print(add(3.5, 7))
    except ValueError as e:
        print(e)
    try:
        print(add("hello", 10))
    except ValueError as e:
        print(e)