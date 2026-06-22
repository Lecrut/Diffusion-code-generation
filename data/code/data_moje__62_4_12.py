def get_divisors(n):
    return [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
    return sorted(list(set(divs + [n // d for d in divs])))

if __name__ == '__main__':
    result = get_divisors(60)
    print(result)