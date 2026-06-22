def count_even_numbers(start, end):
    if start > end:
        return 0
    count = (end - start + 1) // 2
    if (end - start + 1) % 2 == 1 and start % 2 == 0:
        count += 1
    return count

if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    result2 = count_even_numbers(5, 15)
    result3 = count_even_numbers(2, 2)
    result4 = count_even_numbers(3, 3)
    print(result1)
    print(result2)
    print(result3)
    print(result4)