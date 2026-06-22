def add_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    x = 15
    y = 25
    try:
        result = add_integers(x, y)
        print(result)
    except ValueError as e:
        print(e)