def count_even_numbers(a, b):
    low, high = (a, b) if a <= b else (b, a)
    first_even = low + 1 if low % 2 != 0 else low
    if first_even > high:
        return 0
    last_even = high - 1 if high % 2 != 0 else high
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(10, 1))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(2, 2))