def is_proportional(a, b, c, d):
    return a * d == b * c

def simplify_ratio(a, b):
    gcd = abs(a)
    for i in range(gcd, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    return (a // gcd, b // gcd)

if __name__ == '__main__':
    a, b, c, d = 2, 4, 3, 6
    if is_proportional(a, b, c, d):
        print(f"The numbers are in proportion. Simplified ratio: {simplify_ratio(a, b)}")
    else:
        print("The numbers are not in proportion.")