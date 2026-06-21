def gcd(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")
    
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    num1 = 48
    num2 = 18
    result = gcd(num1, num2)
    print(f"GCD of {num1} and {num2} is: {result}")