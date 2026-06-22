def get_divisors(n):
    if n == 0:
        return []
    abs_n = abs(n)
    divisors = set()
    for i in range(1, int(abs_n**0.5) + 1):
        if abs_n % i == 0:
            divisors.add(i)
            divisors.add(abs_n // i)
    result = list(divisors)
    result.sort()
    if n < 0:
        return [-x for x in result] + result
    return result

if __name__ == '__main__':
    sample_value = 100
    print(get_divisors(sample_value))