def count_even_numbers(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) >> 1 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(5, 15))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(3, 3))
    print(count_even_numbers(10, 1))