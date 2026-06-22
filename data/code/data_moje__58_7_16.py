def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    if start == end:
        return 1 if start % 2 == 0 else 0
    count = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    print(count_even_in_range(1, 10))
    print(count_even_in_range(-5, 5))
    print(count_even_in_range(3, 3))
    print(count_even_in_range(4, 4))
    print(count_even_in_range(-10, -1))
    print(count_even_in_range(100, 100))
    print(count_even_in_range(0, 0))
    print(count_even_in_range(1, 1))