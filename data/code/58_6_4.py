def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    first_even = min_val + (min_val % 2)
    if first_even > max_val:
        return 0
    last_even = max_val - (max_val % 2)
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 5))
    print(count_even_numbers(3, 3))
    print(count_even_numbers(10, 1))