def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    count = 0
    if start % 2 == 0:
        count = (end - start) // 2 + 1
    else:
        count = (end - start + 1) // 2
    return count

if __name__ == '__main__':
    result = count_even_in_range(1, 10)
    print(result)