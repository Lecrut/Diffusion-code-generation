def count_evens(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(1, 1))
    print(count_evens(5, 5))
    print(count_evens(6, 6))
    print(count_evens(0, 0))
    print(count_evens(-5, 5))
    print(count_evens(-2, 2))