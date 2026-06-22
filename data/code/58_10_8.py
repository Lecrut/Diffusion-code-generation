def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        return 0
    count = (end // 2) - ((start - 1) // 2)
    return count

if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    print(result1)
    result2 = count_even_numbers(5, 15)
    print(result2)
    result3 = count_even_numbers(0, 0)
    print(result3)
    result4 = count_even_numbers(-10, -1)
    print(result4)
    result5 = count_even_numbers(3, 3)
    print(result5)