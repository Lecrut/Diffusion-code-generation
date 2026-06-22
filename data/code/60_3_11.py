def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    sample_inputs = [0, 1, 5, 10, 20, 50]
    results = [factorial(n) for n in sample_inputs]
    for n, res in zip(sample_inputs, results):
        print(f"factorial({n}) = {res}")