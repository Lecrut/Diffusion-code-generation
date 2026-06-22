def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    result = 1
    counter = 1
    while counter <= n:
        result *= counter
        counter += 1
    return result

if __name__ == '__main__':
    print(compute_factorial(5))
    print(compute_factorial(0))
    print(compute_factorial(10))