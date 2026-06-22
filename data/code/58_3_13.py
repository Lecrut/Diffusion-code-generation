def count_even_integers(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_integers(1, 10))
    print(count_even_integers(2, 8))
    print(count_even_integers(3, 3))
    print(count_even_integers(5, 5))
    print(count_even_integers(10, 1))