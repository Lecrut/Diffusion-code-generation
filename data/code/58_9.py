def count_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    if start > end:
        return 0
    count_upto_end = end // 2 - (end % 2 + 1) // 2 + 1
    count_upto_start_minus_one = (start - 1) // 2 - ((start - 1) % 2 + 1) // 2 + 1
    return count_upto_end - count_upto_start_minus_one

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(3, 7))
    print(count_even_numbers(10, 1))