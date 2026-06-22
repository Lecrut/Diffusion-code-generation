def count_evens(start, end):
    if start > end:
        return 0
    count = end // 2 - (start - 1) // 2
    return count

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(3, 7))
    print(count_evens(2, 2))
    print(count_evens(5, 5))
    print(count_evens(10, 1))