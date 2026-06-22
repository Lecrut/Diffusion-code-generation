def count_evens(low: int, high: int) -> int:
    if low > high:
        return 0
    first_even = low if low % 2 == 0 else low + 1
    if first_even > high:
        return 0
    last_even = high if high % 2 == 0 else high - 1
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    low_value = 3
    high_value = 10
    result = count_evens(low_value, high_value)
    print(result)