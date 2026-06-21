def gcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative")
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    sample_a = 56
    sample_b = 98
    result = gcd(sample_a, sample_b)
    print(f"GCD of {sample_a} and {sample_b} is: {result}")