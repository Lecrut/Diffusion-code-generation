def check_proportion(a, b, c, d):
    if a * d == b * c:
        gcd = abs(a)
        while gcd > 1:
            if (a % gcd == 0) and (b % gcd == 0) and (c % gcd == 0) and (d % gcd == 0):
                break
            gcd -= 1
        return f"{a//gcd}:{b//gcd}:{c//gcd}:{d//gcd}"
    else:
        return "Not in proportion"

if __name__ == '__main__':
    print(check_proportion(4, 8, 6, 12))