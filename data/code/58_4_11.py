def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        return 0
    start = low if low % 2 == 0 else low + 1
    if start > high:
        return 0
    return (high - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(10, 20)
    print(result)