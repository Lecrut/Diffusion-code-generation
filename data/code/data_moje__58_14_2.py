def count_evens(start, end):
    lo = min(start, end)
    hi = max(start, end)
    first_even = lo + (lo % 2)
    last_even = hi - ((hi + 1) % 2)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    a = 3
    b = 10
    print(count_evens(a, b))