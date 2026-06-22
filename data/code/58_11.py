def count_even_inclusive(low: int, high: int) -> int:
    if low > high:
        return 0
    start = low if low % 2 == 0 else low + 1
    end = high if high % 2 == 0 else high - 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_inclusive(2, 10)
    print(result)