import math
def calculate_sqrt_and_factorial(n):
    sqrt_n = math.sqrt(n)
    factorial_n = math.factorial(n)
    return sqrt_n, factorial_n
if __name__ == '__main__':
    number = 5
    sqrt_result, factorial_result = calculate_sqrt_and_factorial(number)
    print(f"Square root of {number}: {sqrt_result}")
    print(f"Factorial of {number}: {factorial_result}")