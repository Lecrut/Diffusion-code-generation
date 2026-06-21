def add(a, b):
    try:
        return a + b
    except TypeError:
        raise ValueError("Both arguments must be numbers")

if __name__ == '__main__':
    try:
        print(add(5, 15))
    except ValueError as e:
        print(e)