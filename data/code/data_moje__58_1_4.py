def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    lower = a + 1 if a % 2 != 0 else a
    upper = b - 1 if b % 2 != 0 else b
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 9)
    print(result)
    result2 = count_even_numbers(10, 2)
    print(result2)
    result3 = count_even_numbers(7, 7)
    print(result3)
    result4 = count_even_numbers(-5, 5)
    print(result4)