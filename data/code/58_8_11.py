def count_even_numbers(a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    if min_val > max_val:
        return 0
    first_even = min_val if min_val % 2 == 0 else min_val + 1
    last_even = max_val if max_val % 2 == 0 else max_val - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(5, 15))
    print(count_even_numbers(10, 10))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(-5, 5))