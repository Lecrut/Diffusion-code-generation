def count_even_numbers(a, b):
    low = min(a, b)
    high = max(a, b)
    first_even = low if low % 2 == 0 else low + 1
    if first_even > high:
        return 0
    last_even = high if high % 2 == 0 else high - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    a = 1
    b = 10
    print(count_even_numbers(a, b))