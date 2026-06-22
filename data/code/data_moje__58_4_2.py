def count_even(low: int, high: int) -> int:
    if low > high:
        return 0
    count = 0
    start = low if low % 2 == 0 else low + 1
    end = high if high % 2 == 0 else high - 1
    if start <= end:
        count = (end - start) // 2 + 1
    return count

if __name__ == '__main__':
    low = 3
    high = 10
    result = count_even(low, high)
    print(result)