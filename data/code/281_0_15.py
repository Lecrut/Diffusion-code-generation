def validate_input(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return a, b, c

def sum_three(a, b, c):
    a, b, c = validate_input(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result = sum_three(10, 25, 30)
    print(result)