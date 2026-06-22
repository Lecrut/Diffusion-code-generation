def power(base, exp):
    if exp < 0:
        return 1 / power(base, -exp)
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        return base * power(base, exp - 1)

if __name__ == '__main__':
    result = power(2, 10)
    print(result)
    result = power(3, 5)
    print(result)
    result = power(5, -2)
    print(result)