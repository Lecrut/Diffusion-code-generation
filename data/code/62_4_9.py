def get_divisors(n):
    divisors = [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
    all_divisors = set()
    for d in divisors:
        all_divisors.add(d)
        all_divisors.add(n // d)
    return sorted(list(all_divisors))

if __name__ == '__main__':
    result = get_divisors(60)
    print(result)