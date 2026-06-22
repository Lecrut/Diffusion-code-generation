def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)