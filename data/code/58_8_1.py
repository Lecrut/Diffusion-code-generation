def count_even_numbers(a, b):
    start = max(a, b)
    end = min(a, b)
    if start % 2 != 0:
        start -= 1
    if end % 2 != 0:
        end += 1
    if start < end:
        return 0
    return (start - end) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 8))
    print(count_even_numbers(3, 7))
    print(count_even_numbers(10, 1))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(-5, 5))