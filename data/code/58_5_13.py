def count_even_numbers(start, end):
    if start > end:
        return 0
    count = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            count += 1
    return count

def count_even_numbers_math(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    result_math = count_even_numbers_math(sample_start, sample_end)
    print(result_math)