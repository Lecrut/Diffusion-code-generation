def count_even_numbers(start, end):
    if start > end:
        return 0
    if start % 2 == 0:
        first = start
    else:
        first = start + 1
    if end % 2 == 0:
        last = end
    else:
        last = end - 1
    if first > last:
        return 0
    return ((last - first) >> 1) + 1

if __name__ == '__main__':
    range_start = 10
    range_end = 50
    result = count_even_numbers(range_start, range_end)
    print(result)