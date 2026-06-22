def count_evens(start, end):
    if start > end:
        return 0
    adjusted_start = start if start % 2 == 0 else start + 1
    adjusted_end = end if end % 2 == 0 else end - 1
    if adjusted_start > adjusted_end:
        return 0
    return (adjusted_end - adjusted_start) // 2 + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(13, 20))