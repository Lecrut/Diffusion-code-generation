def count_even_numbers(a, b):
    low = min(a, b)
    high = max(a, b)
    first_even = low + (low % 2)
    last_even = high - (high % 2)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(5, 15))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(10, 1))