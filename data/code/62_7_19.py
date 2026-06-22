def get_divisors(n):
    if n == 0:
        return []
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if n > 0 and i != 1 and i != n:
                divisors.append(-i)
            elif n < 0:
                divisors.append(-i)
                if i != 1:
                    divisors.append(i)
    if n < 0:
        divisors.sort()
    return divisors

if __name__ == '__main__':
    print(get_divisors(0))