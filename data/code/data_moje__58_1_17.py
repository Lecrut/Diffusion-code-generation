def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    return (b // 2) - ((a - 1) // 2)

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result = count_even_numbers(10, 1)
    print(result)
    result = count_even_numbers(2, 2)
    print(result)
    result = count_even_numbers(3, 3)
    print(result)
    result = count_even_numbers(-5, 5)
    print(result)