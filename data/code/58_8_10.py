def count_evens(start, end):
    if start > end:
        return 0
    if start == end:
        return 1 if start % 2 == 0 else 0
    low = (start + 1) if start % 2 != 0 else start
    high = end if end % 2 == 0 else (end - 1)
    if low > high:
        return 0
    return (high - low) // 2 + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 8))
    print(count_evens(11, 11))
    print(count_evens(5, 4))