def count_even_integers(start, end):
    if start > end:
        start, end = end, start
    count_end = end // 2
    count_start = (start - 1) // 2
    return count_end - count_start

if __name__ == '__main__':
    lower_bound = 5
    upper_bound = 20
    result = count_even_integers(lower_bound, upper_bound)
    print(result)