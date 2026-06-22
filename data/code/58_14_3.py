def count_even_numbers(start, end):
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
    lower_bound = 10
    upper_bound = 50
    result = count_even_numbers(lower_bound, upper_bound)
    print(result)