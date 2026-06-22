def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        return 0
    if low % 2 != 0:
        first_even = low + 1
    else:
        first_even = low
    if high % 2 != 0:
        last_even = high - 1
    else:
        last_even = high
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1
if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    print(result1)
    result2 = count_even_numbers(-5, 5)
    print(result2)
    result3 = count_even_numbers(2, 2)
    print(result3)
    result4 = count_even_numbers(3, 3)
    print(result4)
    result5 = count_even_numbers(0, 100)
    print(result5)