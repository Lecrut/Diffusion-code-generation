def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    first_even = a + (1 if a % 2 != 0 else 0)
    if first_even > b:
        return 0
    last_even = b - (1 if b % 2 != 0 else 0)
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(10, 1))
    print(count_even_numbers(3, 7))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(1, 1))