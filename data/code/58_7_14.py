def count_evens_in_range(start, end):
    if start > end:
        start, end = end, start
    if start == end:
        return 1 if start % 2 == 0 else 0
    if start % 2 == 0 and end % 2 == 0:
        return (end - start) // 2 + 1
    elif start % 2 != 0 and end % 2 != 0:
        return (end - start) // 2
    else:
        return (end - start) // 2 + 1

if __name__ == '__main__':
    print(count_evens_in_range(1, 10))
    print(count_evens_in_range(-5, 5))
    print(count_evens_in_range(7, 7))
    print(count_evens_in_range(10, 1))
    print(count_evens_in_range(-10, -1))