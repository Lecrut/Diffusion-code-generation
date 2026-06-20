def subtract_values(a=10, b=5):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    return a - b

if __name__ == '__main__':
    result = subtract_values()
    print(result)