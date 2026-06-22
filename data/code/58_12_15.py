def count_even_values(start, end):
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
    result = count_even_values(10, 20)
    print(result)
    result = count_even_values(1, 10)
    print(result)
    result = count_even_values(5, 5)
    print(result)
    result = count_even_values(7, 7)
    print(result)
    result = count_even_values(100, 1)
    print(result)