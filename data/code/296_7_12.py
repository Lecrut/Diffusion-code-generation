def check_proportion(a, b, c, d):
    if a * d == b * c:
        gcd = abs(gcd(a, b, c, d))
        return (a // gcd, b // gcd, c // gcd, d // gcd)
    else:
        return None

def gcd(x, y, z, w):
    while y != 0:
        x, y = y, x % y
    while z != 0:
        x, z = z, x % z
    while w != 0:
        x, w = w, x % w
    return x

if __name__ == '__main__':
    print(check_proportion(4, 8, 6, 12))