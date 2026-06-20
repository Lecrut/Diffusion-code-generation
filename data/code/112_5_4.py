def sum_numbers(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    result = sum_numbers(10, 5)
    print(result)