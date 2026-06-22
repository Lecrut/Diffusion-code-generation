def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    first_even = a if a % 2 == 0 else a + 1
    last_even = b if b % 2 == 0 else b - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 9)
    print(result)