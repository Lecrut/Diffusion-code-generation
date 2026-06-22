def power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        half = power(base, exp // 2)
        return base * half * half

if __name__ == '__main__':
    result = power(2, 100)
    print(result)
    result = power(3, 10)
    print(result)
    result = power(5, 0)
    print(result)