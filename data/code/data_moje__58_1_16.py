def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    if a % 2 != 0:
        a += 1
    if a > b:
        return 0
    return (b - a) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 9)
    print(result)
    result = count_even_numbers(10, 2)
    print(result)
    result = count_even_numbers(5, 5)
    print(result)
    result = count_even_numbers(-3, 4)
    print(result)