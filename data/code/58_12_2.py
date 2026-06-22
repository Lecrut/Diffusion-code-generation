def count_even_values(start, stop):
    if start > stop:
        return 0
    if start % 2 != 0:
        start += 1
    if stop % 2 != 0:
        stop -= 1
    if start > stop:
        return 0
    return (stop - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_values(1, 10)
    print(result)