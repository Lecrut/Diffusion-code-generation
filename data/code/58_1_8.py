def count_even_numbers(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    first_even = a if a % 2 == 0 else a + 1
    if first_even > b:
        return 0
    last_even = b if b % 2 == 0 else b - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 10)
    print(result)