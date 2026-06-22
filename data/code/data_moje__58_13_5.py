def count_even_numbers(start, end):
    if start > end:
        return 0
    count_start = start // 2
    count_end = end // 2
    return count_end - count_start
if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    print(result1)
    result2 = count_even_numbers(2, 2)
    print(result2)
    result3 = count_even_numbers(-5, 5)
    print(result3)
    result4 = count_even_numbers(0, 0)
    print(result4)
    result5 = count_even_numbers(10, 1)
    print(result5)