def power(base, exp):
    if exp < 0:
        return 1 / power(-base, -exp)
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    result = half * half
    if exp % 2 == 1:
        result = result * base
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 5))
    print(power(5, 0))
    print(power(2, -3))