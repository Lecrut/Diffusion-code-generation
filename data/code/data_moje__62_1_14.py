def is_valid_positive_integer(n):
    if not isinstance(n, int):
        return False
    if n <= 0:
        return False
    return True

def collect_divisors(n):
    if not is_valid_positive_integer(n):
        return []
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            counterpart = n // i
            if counterpart != i:
                divisors.append(counterpart)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    target_number = 100
    found_divisors = collect_divisors(target_number)
    print(found_divisors)