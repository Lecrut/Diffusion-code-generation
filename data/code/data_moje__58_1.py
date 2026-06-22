def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    first_even = a if a % 2 == 0 else a + 1
    if first_even > b:
        return 0
    last_even = b if b % 2 == 0 else b - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 9)
    print(result)
    result2 = count_even_numbers(10, 2)
    print(result2)
    result3 = count_even_numbers(5, 5)
    print(result3)