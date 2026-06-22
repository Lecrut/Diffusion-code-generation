def count_even_numbers(start, end):
    if start > end:
        return 0
    if end % 2 != 0:
        end -= 1
    if start % 2 != 0:
        start += 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result = count_even_numbers(2, 8)
    print(result)
    result = count_even_numbers(3, 3)
    print(result)
    result = count_even_numbers(4, 4)
    print(result)
    result = count_even_numbers(10, 1)
    print(result)