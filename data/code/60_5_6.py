def compute_factorial(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    result = 1
    counter = 1
    while counter <= n:
        result = result * counter
        counter = counter + 1
    return result

if __name__ == '__main__':
    print(compute_factorial(5))
    print(compute_factorial(0))
    print(compute_factorial(10))