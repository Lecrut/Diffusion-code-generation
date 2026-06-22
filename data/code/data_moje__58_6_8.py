def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    start = min_val if min_val % 2 == 0 else min_val + 1
    end = max_val if max_val % 2 == 0 else max_val - 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(2, 10)
    print(result)