def compute_factorial(n: int) -> int:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return 1
    acc = 1
    for k in range(2, n + 1):
        acc *= k
    return acc

if __name__ == '__main__':
    print(compute_factorial(0))
    print(compute_factorial(1))
    print(compute_factorial(6))
    print(compute_factorial(9))
    try:
        compute_factorial(-5)
    except ValueError as e:
        print(e)
    try:
        compute_factorial(3.5)
    except TypeError as e:
        print(e)