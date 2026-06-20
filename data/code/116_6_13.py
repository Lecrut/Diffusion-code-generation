def add_three_numbers(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return a + b + c

if __name__ == '__main__':
    try:
        result = add_three_numbers(5, 3, 8)
        print(result)
    except ValueError as e:
        print(e)