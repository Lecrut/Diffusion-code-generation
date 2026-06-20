def sum_even_numbers(start, end):
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    sample_start = 3
    sample_end = 25
    result = sum_even_numbers(sample_start, sample_end)
    print(result)