def check_proportion(a, b, c, d):
    if a * d == b * c:
        gcd = abs(gcd(a, b))
        return (a // gcd, b // gcd, c // gcd, d // gcd)
    else:
        return None

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

if __name__ == '__main__':
    print(check_proportion(4, 8, 6, 12))