def count_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    if start > end:
        return 0
    count_upto_end = (end >> 1) + 1
    count_upto_start_minus_1 = ((start - 1) >> 1) + 1
    return count_upto_end - count_upto_start_minus_1

if __name__ == '__main__':
    lower = 4
    upper = 10
    result = count_even_numbers(lower, upper)
    print(result)