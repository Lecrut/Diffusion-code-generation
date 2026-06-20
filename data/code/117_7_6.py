def subtract_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError('Both inputs must be numbers')
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(15.5, 7)
    print(result)