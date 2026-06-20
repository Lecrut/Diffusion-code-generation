def add_numbers(a, b):
    if not all(isinstance(x, int) for x in [a, b]):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    result = add_numbers(15, 27)
    print(result)