def count_even_numbers(start, end):
    if start > end:
        start, end = end, start
    first_even = start + (start % 2)
    if first_even > end:
        return 0
    return (end - first_even) // 2 + 1

if __name__ == '__main__':
    start_value = 10
    end_value = 30
    result = count_even_numbers(start_value, end_value)
    print(result)