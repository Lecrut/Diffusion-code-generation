def count_even_numbers(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    if first_even > end:
        return 0
    return (end - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result = count_even_numbers(2, 2)
    print(result)
    result = count_even_numbers(1, 1)
    print(result)
    result = count_even_numbers(0, 0)
    print(result)
    result = count_even_numbers(-5, 5)
    print(result)