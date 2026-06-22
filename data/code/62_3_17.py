def get_divisors(n):
    if n == 0:
        return []
    lower = 1
    upper = abs(n)
    result = []
    current = lower
    while current <= upper:
        if n % current == 0:
            result.append(current)
        current += 1
    return result

if __name__ == '__main__':
    target = 1
    output = get_divisors(target)
    print(output)