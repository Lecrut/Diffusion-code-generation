GCD_THRESHOLD = 1

def calculate_gcd(a, b):
    while b != GCD_THRESHOLD:
        if a > b:
            a -= b
        else:
            b -= a
    return a
if __name__ == '__main__':
    result = calculate_gcd(48, 18)
    print(result)