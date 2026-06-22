def count_even_numbers(start, end):
    if start > end:
        return 0
    if start < 0 and end < 0:
        return count_even_numbers(-end, -start)
    if start < 0:
        positive_start = 0
        negative_count = count_even_numbers(start, -1)
        return negative_count + count_even_numbers(0, end)
    start_val = start
    end_val = end
    first_even = start_val if (start_val & 1) == 0 else start_val + 1
    if first_even > end_val:
        return 0
    return ((end_val ^ first_even) >> 1) + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 15)
    print(result)
    result2 = count_even_numbers(2, 10)
    print(result2)
    result3 = count_even_numbers(10, 10)
    print(result3)
    result4 = count_even_numbers(11, 11)
    print(result4)