def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    lower = min_val if min_val % 2 == 0 else min_val + 1
    upper = max_val if max_val % 2 == 0 else max_val - 1
    if lower > upper:
        return 0
    count = ((upper - lower) // 2) + 1
    return count

if __name__ == '__main__':
    min_val = 1
    max_val = 10
    result = count_even_numbers(min_val, max_val)
    print(result)