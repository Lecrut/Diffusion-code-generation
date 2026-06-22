def count_even_numbers(start, end):
    if start > end:
        start, end = end, start
    if start < 0:
        start = -start
    if start % 2 != 0:
        start += 1
    if end < 0:
        end = -end
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)