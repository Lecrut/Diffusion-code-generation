def validate_inputs(a, b, c):
    if not all(isinstance(i, int) for i in (a, b, c)):
        raise ValueError("All inputs must be integers")
    return True

def sum_three(a, b, c):
    validate_inputs(a, b, c)
    return a + b + c

if __name__ == '__main__':
    print(sum_three(1, 2, 3))