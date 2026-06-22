def get_divisors(n):
    return [i for i in range(1, int(n**0.5) + 1) if n % i == 0] + [n // i for i in range(1, int(n**0.5) + 1) if n % i == 0 and i != n // i]

def get_sorted_divisors(n):
    divs = get_divisors(n)
    divs.sort()
    return divs

if __name__ == '__main__':
    target_number = 60
    result = get_sorted_divisors(target_number)
    print(result)