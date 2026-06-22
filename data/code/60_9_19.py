def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    accumulator = 1
    current_number = 1
    while current_number <= n:
        accumulator *= current_number
        current_number += 1
    return accumulator

if __name__ == '__main__':
    test_values = [3, 4, 6, 8]
    for value in test_values:
        output = factorial(value)
        print(output)