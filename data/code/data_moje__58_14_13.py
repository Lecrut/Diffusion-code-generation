def count_even_numbers(start, end):
    if start > end:
        return 0
    count_start = (start - 1) // 2
    count_end = end // 2
    return count_end - count_start

if __name__ == '__main__':
    low = 3
    high = 15
    result = count_even_numbers(low, high)
    print(result)