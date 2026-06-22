def count_even_numbers(low: int, high: int) -> int:
    start = low if low % 2 == 0 else low + 1
    end = high if high % 2 == 0 else high - 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    low_val = 1
    high_val = 10
    result = count_even_numbers(low_val, high_val)
    print(result)