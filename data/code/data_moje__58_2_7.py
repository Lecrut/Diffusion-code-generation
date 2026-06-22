def count_even_numbers(start, end):
    if start > end:
        start, end = end, start
    adjusted_start = start + (start & 1)
    if adjusted_start > end:
        return 0
    return (end - adjusted_start) >> 1 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)