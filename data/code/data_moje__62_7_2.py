def get_divisors(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == -1:
        return [-1, 1]
    
    divisors = set()
    abs_n = abs(n)
    i = 1
    while i * i <= abs_n:
        if abs_n % i == 0:
            divisors.add(i)
            divisors.add(abs_n // i)
            if n < 0:
                divisors.add(-i)
                divisors.add(-(abs_n // i))
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    print(get_divisors(0))
    print(get_divisors(12))
    print(get_divisors(-12))
    print(get_divisors(1))
    print(get_divisors(-1))