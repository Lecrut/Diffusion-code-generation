def _validate_integer(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n

def find_divisors(n):
    _validate_integer(n)
    n = abs(n)
    if n == 0:
        return [0]
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    number = 36
    result = find_divisors(number)
    print(result)