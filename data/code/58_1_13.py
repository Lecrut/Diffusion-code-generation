def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(3, 10))
    print(count_even_numbers(10, 3))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(-5, 5))