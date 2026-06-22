def count_even(start, end):
    if start > end:
        return 0
    first = start if start % 2 == 0 else start + 1
    last = end if end % 2 == 0 else end - 1
    if first > last:
        return 0
    return (last - first) // 2 + 1

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)