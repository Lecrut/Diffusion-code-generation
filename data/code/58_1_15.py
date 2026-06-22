def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    if a % 2 != 0:
        a += 1
    if a > b:
        return 0
    return (b - a) // 2 + 1

if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    print(result1)
    result2 = count_even_numbers(10, 1)
    print(result2)
    result3 = count_even_numbers(5, 5)
    print(result3)
    result4 = count_even_numbers(2, 2)
    print(result4)
    result5 = count_even_numbers(-5, 5)
    print(result5)