def count_even_integers(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    if first_even > end:
        return 0
    last_even = end if end % 2 == 0 else end - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_integers(3, 9))
    print(count_even_integers(-5, 5))
    print(count_even_integers(4, 4))
    print(count_even_integers(5, 5))
    print(count_even_integers(10, 2))