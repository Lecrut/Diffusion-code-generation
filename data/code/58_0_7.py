def count_evens(start, end):
    if start > end:
        return 0
    if start % 2 == 0:
        return (end - start) // 2 + 1
    else:
        return (end - start) // 2 + (1 if end % 2 == 0 else 0)

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(3, 3))
    print(count_evens(0, 0))
    print(count_evens(-5, 5))