def get_divisors(n):
    return [i for i in range(1, int(n**0.5) + 1) if n % i == 0 for j in ([i, n // i] if i != n // i else [i])]

def flatten_divisors(divisor_list):
    flattened = []
    for items in divisor_list:
        for item in items:
            flattened.append(item)
    return sorted(flattened)

def get_all_divisors(n):
    raw_divisors = get_divisors(n)
    return flatten_divisors(raw_divisors)

if __name__ == '__main__':
    number = 28
    result = get_all_divisors(number)
    print(result)