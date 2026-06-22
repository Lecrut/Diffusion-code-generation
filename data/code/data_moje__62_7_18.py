def find_divisors(n):
    if n == 0:
        return []
    upper_bound = abs(n)
    candidates = []
    index = 1
    while index * index <= upper_bound:
        if upper_bound % index == 0:
            candidates.append(index)
            if index * index != upper_bound:
                candidates.append(upper_bound // index)
        index += 1
    if n < 0:
        candidates = [-c for c in candidates]
    return sorted(candidates)

if __name__ == '__main__':
    result_zero = find_divisors(0)
    result_negative = find_divisors(-36)
    result_positive = find_divisors(42)
    print(result_zero)
    print(result_negative)
    print(result_positive)