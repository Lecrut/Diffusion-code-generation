def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    
    while b != 0:
        a, b = b, a % b
    
    return abs(a)

if __name__ == '__main__':
    num1 = 48
    num2 = 18
    result = gcd(num1, num2)
    print(f"GCD of {num1} and {num2} is: {result}")