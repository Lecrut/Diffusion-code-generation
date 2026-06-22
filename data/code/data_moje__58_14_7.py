def count_even_numbers(a, b):
    low = min(a, b)
    high = max(a, b)
    first_even = low if low % 2 == 0 else low + 1
    last_even = high if high % 2 == 0 else high - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))