def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        low, high = high, low
    count = 0
    current = low
    while current <= high:
        if current % 2 == 0:
            count += 1
        current += 1
    return count

if __name__ == '__main__':
    result = count_even_numbers(3, 10)
    print(result)