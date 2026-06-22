def divisors(n):
    if n == 0:
        return []
    result = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)
            if i != abs(n) and i != 0:
                result.append(-i)
    if n > 0:
        result.extend([-i for i in result if i > 0] if n < 0 else [])
    return sorted(set(result)) if n != 0 else []

if __name__ == '__main__':
    print(divisors(0))
    print(divisors(12))
    print(divisors(-12))
    print(divisors(1))
    print(divisors(7))