def count_evens(start, end):
    if start > end:
        return 0
    lower = start + (start % 2 != 0)
    upper = end - (end % 2 != 0)
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    result = count_evens(2, 10)
    print(result)