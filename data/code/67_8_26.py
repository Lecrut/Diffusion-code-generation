def sum_values(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        print(sum_values(15, 25))
    except ValueError as e:
        print(e)