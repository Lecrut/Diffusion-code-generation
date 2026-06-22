def count_even_numbers(start, end):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise TypeError("Start and end must be numeric values")
    if start > end:
        start, end = end, start
    start = int(start)
    end = int(end)
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result2 = count_even_numbers(2, 2)
    print(result2)
    result3 = count_even_numbers(1, 1)
    print(result3)
    result4 = count_even_numbers(-5, 5)
    print(result4)
    result5 = count_even_numbers(0, 0)
    print(result5)