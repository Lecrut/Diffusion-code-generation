def count_even_numbers(start, stop):
    if start > stop:
        return 0
    if start % 2 != 0:
        start += 1
    count = (stop - start) // 2 + 1
    if start > stop:
        return 0
    return count

if __name__ == '__main__':
    start_value = 1
    end_value = 10
    result = count_even_numbers(start_value, end_value)
    print(result)