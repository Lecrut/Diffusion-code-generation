def count_even_numbers(start, end):
    if start > end:
        return 0
    first_even = start + (start & 1)
    if first_even > end:
        return 0
    count = ((end - first_even) >> 1) + 1
    return count

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)