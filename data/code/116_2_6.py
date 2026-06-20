def sum_three(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return a + b + c

if __name__ == '__main__':
    x = 10
    y = 20
    z = 30
    result = sum_three(x, y, z)
    print(result)