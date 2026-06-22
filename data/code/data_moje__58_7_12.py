def count_even_integers(start, end):
    if start > end:
        start, end = end, start
    if start % 2 == 0:
        first_even = start
    else:
        first_even = start + 1
    if end % 2 == 0:
        last_even = end
    else:
        last_even = end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_integers(1, 10))
    print(count_even_integers(-5, 5))
    print(count_even_integers(2, 2))
    print(count_even_integers(3, 3))
    print(count_even_integers(1, 1))
    print(count_even_integers(-10, -1))
    print(count_even_integers(100, 200))
    print(count_even_integers(7, 7))
    print(count_even_integers(0, 0))
    print(count_even_integers(-1, 1))