def add_two_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    try:
        result = add_two_integers(10, 25)
        print(result)
    except ValueError as e:
        print(e)