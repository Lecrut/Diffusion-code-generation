def count_even_numbers(start, end):
    if start > end:
        return 0
    return (end // 2) - ((start - 1) // 2)

if __name__ == '__main__':
    print(count_even_numbers(10, 20))
    print(count_even_numbers(3, 15))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(2, 2))