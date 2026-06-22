def add_integers(a, b):
    if not all(isinstance(i, int) for i in (a, b)):
        raise ValueError("Both arguments must be integers.")
    return a + b

if __name__ == '__main__':
    result = add_integers(3, 5)
    print(result)