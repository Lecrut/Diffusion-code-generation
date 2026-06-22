def count_evens(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    return max(0, (end - start) // 2 + 1)

if __name__ == '__main__':
    print(count_evens(2, 8))
    print(count_evens(1, 10))
    print(count_evens(3, 3))
    print(count_evens(10, 1))