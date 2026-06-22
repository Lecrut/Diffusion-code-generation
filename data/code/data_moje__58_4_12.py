def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        return 0
    count = 0
    current = low
    while current <= high:
        if current % 2 == 0:
            count += 1
        current += 1
    return count

if __name__ == '__main__':
    low_bound = 1
    high_bound = 10
    result = count_even_numbers(low_bound, high_bound)
    print(result)