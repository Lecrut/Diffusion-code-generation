def count_even_numbers(start, end):
    if start > end:
        return 0
    if start % 2 == 0:
        return (end - start) // 2 + 1
    else:
        return (end - start + 1) // 2

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 9))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(10, 1))