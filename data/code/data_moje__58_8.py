def count_evens(start, end):
    if start > end:
        start, end = end, start
    low = start if start % 2 == 0 else start + 1
    high = end if end % 2 == 0 else end - 1
    if low > high:
        return 0
    return (high - low) // 2 + 1

if __name__ == '__main__':
    result = count_evens(3, 10)
    print(result)