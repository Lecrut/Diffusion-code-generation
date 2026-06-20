def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    print(calculate_gcd(48, 18))