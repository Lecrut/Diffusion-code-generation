def get_divisors(n):
    return [i for i in range(1, int(n**0.5) + 1) if n % i == 0 for j in ([i, n // i] if i != n // i else [i])] if n > 0 else []

def get_sorted_divisors(n):
    divs = [i for i in range(1, int(n**0.5) + 1) if n % i == 0 for j in ([i, n // i] if i != n // i else [i])]
    return sorted(set(divs))

if __name__ == '__main__':
    result = get_sorted_divisors(60)
    print(result)