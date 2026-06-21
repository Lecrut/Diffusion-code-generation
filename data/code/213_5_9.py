def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == '__main__':
    sample_a = 48
    sample_b = 18
    result = gcd(sample_a, sample_b)
    print(f"GCD of {sample_a} and {sample_b}: {result}")