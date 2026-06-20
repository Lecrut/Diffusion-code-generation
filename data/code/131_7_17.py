def gcd_iterative(a, b):
    while b:
        a, b = (b, a % b)
    return a
if __name__ == '__main__':
    result = gcd_iterative(48, 18)
    print(result)