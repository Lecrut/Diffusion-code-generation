def count_evens_in_range(start, end):
    if start > end:
        start, end = end, start
    if start % 2 == 0:
        first_even = start
    else:
        first_even = start + 1
    if end % 2 == 0:
        last_even = end
    else:
        last_even = end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_evens_in_range(1, 10)
    print(result)