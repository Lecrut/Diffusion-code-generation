def _validate_input(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    return n

def find_divisors(n):
    _validate_input(n)
    divisors = []
    limit = int(n ** 0.5)
    for candidate in range(1, limit + 1):
        if n % candidate == 0:
            divisors.append(candidate)
            second_factor = n // candidate
            if second_factor != candidate:
                divisors.append(second_factor)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    target = 48
    output = find_divisors(target)
    print(output)