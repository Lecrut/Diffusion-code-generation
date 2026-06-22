def get_divisors(n):
    if n == 0:
        return []
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    print(get_divisors(0))
    print(get_divisors(12))