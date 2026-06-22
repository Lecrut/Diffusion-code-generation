def count_evens(start, end):
    if start > end:
        return 0
    def count(n):
        return n // 2
    return count(end) - count(start - 1)

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 8))
    print(count_evens(5, 5))
    print(count_evens(10, 1))