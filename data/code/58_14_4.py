def count_even_numbers(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    start_even = a if a % 2 == 0 else a + 1
    end_even = b if b % 2 == 0 else b - 1
    if start_even > end_even:
        return 0
    return (end_even - start_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)