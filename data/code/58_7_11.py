def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    if start == end:
        return 1 if start % 2 == 0 else 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    print(count_even_in_range(1, 10))
    print(count_even_in_range(-5, 5))
    print(count_even_in_range(2, 2))
    print(count_even_in_range(3, 3))
    print(count_even_in_range(5, 1))
    print(count_even_in_range(-10, -1))
    print(count_even_in_range(0, 0))
    print(count_even_in_range(1, 1))