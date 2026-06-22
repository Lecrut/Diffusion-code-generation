def count_evens(start, end):
    if start > end:
        start, end = end, start
    first_even = start + (1 if start % 2 != 0 else 0)
    last_even = end - (1 if end % 2 != 0 else 0)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(3, 3))
    print(count_evens(4, 4))
    print(count_evens(5, 5))
    print(count_evens(10, 1))
    print(count_evens(0, 0))
    print(count_evens(-5, 5))