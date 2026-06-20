def validate_input(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All inputs must be integers")

def add_three_numbers(a, b, c):
    validate_input(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result = add_three_numbers(5, 3, 8)
    print(result)