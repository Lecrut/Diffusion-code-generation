def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == '__main__':
    num1 = 56
    num2 = 98
    result = gcd(num1, num2)
    print(f"GCD of {num1} and {num2} is: {result}")