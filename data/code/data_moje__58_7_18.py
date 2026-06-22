def count_even_in_range(start, stop):
    if start > stop:
        start, stop = stop, start
    if start % 2 != 0:
        start += 1
    if start > stop:
        return 0
    return (stop - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_in_range(3, 7)
    print(result)