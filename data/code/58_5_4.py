def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    count = 0
    current = start
    while current <= end:
        if current % 2 == 0:
            count += 1
        current += 1
    return count

if __name__ == '__main__':
    result = count_even_in_range(1, 10)
    print(result)