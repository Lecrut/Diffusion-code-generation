def count_even_numbers_bitwise(start, end):
    if start > end:
        start, end = end, start
    count = 0
    if start % 2 != 0:
        count += 1
        start += 1
    while start <= end:
        count += 1
        start += 2
    return count

if __name__ == '__main__':
    result = count_even_numbers_bitwise(1, 10)
    print(result)