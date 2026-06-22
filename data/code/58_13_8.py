def count_even_numbers(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result_1 = count_even_numbers(1, 10)
    print(result_1)
    result_2 = count_even_numbers(5, 5)
    print(result_2)
    result_3 = count_even_numbers(4, 4)
    print(result_3)
    result_4 = count_even_numbers(10, 1)
    print(result_4)