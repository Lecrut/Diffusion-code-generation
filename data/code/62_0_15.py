def find_divisors(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    result = []
    upper = int(n ** 0.5)
    for candidate in range(1, upper + 1):
        if n % candidate == 0:
            result.append(candidate)
            complement = n // candidate
            if candidate != complement:
                result.append(complement)
    return sorted(result)

if __name__ == '__main__':
    sample_value = 36
    divs = find_divisors(sample_value)
    print(divs)