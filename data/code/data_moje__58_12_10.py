def count_evens(start, stop):
    if start > stop:
        return 0
    count = 0
    first_even = start if start % 2 == 0 else start + 1
    if first_even <= stop:
        count = (stop - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_evens(2, 10)
    print(result)