def count_evens(start, end):
    if start > end:
        return 0
    count_before_start = (start - 1) // 2
    count_before_end = end // 2
    return count_before_end - count_before_start

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 10))
    print(count_evens(3, 3))
    print(count_evens(5, 5))
    print(count_evens(10, 1))