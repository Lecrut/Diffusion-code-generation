def count_even_numbers(start, end):
    if start > end:
        return 0
    count_to_end = end // 2
    count_to_start_minus_one = (start - 1) // 2
    return count_to_end - count_to_start_minus_one

if __name__ == '__main__':
    start_val = 10
    end_val = 20
    result = count_even_numbers(start_val, end_val)
    print(result)