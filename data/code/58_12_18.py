def count_even_values(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_values(3, 10)
    print(result)
    result2 = count_even_values(2, 8)
    print(result2)
    result3 = count_even_values(5, 5)
    print(result3)
    result4 = count_even_values(10, 3)
    print(result4)