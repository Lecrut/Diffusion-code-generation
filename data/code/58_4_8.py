def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        return 0
    count_high = high // 2
    count_low = (low - 1) // 2
    return count_high - count_low
if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result2 = count_even_numbers(5, 15)
    print(result2)
    result3 = count_even_numbers(10, 20)
    print(result3)