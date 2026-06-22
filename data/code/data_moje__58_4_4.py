def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        return 0
    first_even = low if low % 2 == 0 else low + 1
    last_even = high if high % 2 == 0 else high - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)