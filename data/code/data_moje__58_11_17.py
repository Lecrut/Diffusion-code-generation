def count_even_between(low: int, high: int) -> int:
    if low > high:
        low, high = high, low
    low_adj = low if low % 2 == 0 else low + 1
    high_adj = high if high % 2 == 0 else high - 1
    if low_adj > high_adj:
        return 0
    return (high_adj - low_adj) // 2 + 1

if __name__ == '__main__':
    result = count_even_between(1, 10)
    print(result)