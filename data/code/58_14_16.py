def count_even_numbers(a, b):
    lo = min(a, b)
    hi = max(a, b)
    first_even = lo + (lo % 2)
    if first_even > hi:
        return 0
    last_even = hi - (hi % 2)
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    a = 3
    b = 15
    print(count_even_numbers(a, b))