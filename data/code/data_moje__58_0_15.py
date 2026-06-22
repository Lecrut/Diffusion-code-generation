def count_evens(start, end):
    if start > end:
        return 0
    first_even = start + (start % 2)
    last_even = end - (end % 2)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(3, 3))
    print(count_evens(2, 2))
    print(count_evens(1, 1))
    print(count_evens(10, 1))