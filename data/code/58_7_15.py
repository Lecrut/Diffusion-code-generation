def count_even_integers(start, end):
    if start > end:
        start, end = end, start
    count = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    print(count_even_integers(1, 10))
    print(count_even_integers(-5, 5))
    print(count_even_integers(7, 7))
    print(count_even_integers(0, 0))
    print(count_even_integers(2, 2))
    print(count_even_integers(-10, -1))
    print(count_even_integers(3, 8))