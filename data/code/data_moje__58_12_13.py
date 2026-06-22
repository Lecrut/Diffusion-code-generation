def count_evens(start, stop):
    if start > stop:
        return 0
    adjusted_start = start if start % 2 == 0 else start + 1
    adjusted_stop = stop if stop % 2 == 0 else stop - 1
    if adjusted_start > adjusted_stop:
        return 0
    return (adjusted_stop - adjusted_start) // 2 + 1

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)
    result = count_evens(2, 2)
    print(result)
    result = count_evens(3, 7)
    print(result)