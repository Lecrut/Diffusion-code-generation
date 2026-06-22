def count_even_integers(a, b):
    if a > b:
        a, b = (b, a)
    first_even = a if a % 2 == 0 else a + 1
    last_even = b if b % 2 == 0 else b - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1
if __name__ == '__main__':
    result1 = count_even_integers(1, 10)
    print(result1)
    result2 = count_even_integers(5, 15)
    print(result2)
    result3 = count_even_integers(2, 2)
    print(result3)
    result4 = count_even_integers(3, 3)
    print(result4)
    result5 = count_even_integers(-10, 10)
    print(result5)
    result6 = count_even_integers(7, 1)
    print(result6)