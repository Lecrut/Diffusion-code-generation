def count_even_numbers(start: int, end: int) -> int:
    low = min(start, end)
    high = max(start, end)
    start_even = low if low % 2 == 0 else low + 1
    end_even = high if high % 2 == 0 else high - 1
    if start_even > end_even:
        return 0
    return (end_even - start_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(2, 10)
    print(result)