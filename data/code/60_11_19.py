def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial argument must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    accumulator = 1
    for current in range(1, n + 1):
        accumulator *= current
    return accumulator

if __name__ == '__main__':
    TARGET = 20
    answer = compute_factorial(TARGET)
    print(answer)