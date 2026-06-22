def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('Input must be an integer.')
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers.')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
if __name__ == '__main__':
    sample_values = [0, 1, 5, 10, 20]
    for value in sample_values:
        print(f'{value}! = {factorial(value)}')