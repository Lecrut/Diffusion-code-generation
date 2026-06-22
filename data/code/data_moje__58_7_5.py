def count_even_integers(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    print(count_even_integers(1, 10))
    print(count_even_integers(-5, 5))
    print(count_even_integers(4, 4))
    print(count_even_integers(5, 5))
    print(count_even_integers(-10, -4))
    print(count_even_integers(10, 5))