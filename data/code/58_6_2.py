def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    first_even = min_val if min_val % 2 == 0 else min_val + 1
    if first_even > max_val:
        return 0
    last_even = max_val if max_val % 2 == 0 else max_val - 1
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    min_sample = 3
    max_sample = 10
    result = count_even_numbers(min_sample, max_sample)
    print(result)