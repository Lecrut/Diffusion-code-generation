def validate_input(a, b, c):
    if not all(isinstance(i, int) for i in (a, b, c)):
        raise ValueError("All inputs must be integers")

def sum_three_integers(a, b, c):
    validate_input(a, b, c)
    return a + b + c

if __name__ == '__main__':
    x = 10
    y = 20
    z = 30
    result = sum_three_integers(x, y, z)
    print(result)