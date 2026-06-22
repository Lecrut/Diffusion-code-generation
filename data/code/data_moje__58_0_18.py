def count_evens(start, end):
    if start > end:
        return 0
    low = (start + 1) // 2
    high = end // 2
    return high - low + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(1, 1))