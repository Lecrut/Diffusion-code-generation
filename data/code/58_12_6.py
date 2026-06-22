def count_even_numbers(start, end):
    if start > end:
        return 0
    count = 0
    if start % 2 == 0:
        first_even = start
    else:
        first_even = start + 1
    if first_even > end:
        return 0
    last_even = end if end % 2 == 0 else end - 1
    count = ((last_even - first_even) // 2) + 1
    return count

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)