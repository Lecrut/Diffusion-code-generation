def count_evens(start, end):
    if start > end:
        start, end = end, start
    if start % 2 == 0:
        start_evens = 1
    else:
        start_evens = 0
    if end % 2 == 0:
        end_evens = 1
    else:
        end_evens = 0
    return (end - start) // 2 + start_evens + end_evens - 1 + (1 if start % 2 != 0 and end % 2 != 0 else 0)

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(1, 1))
    print(count_evens(0, 5))
    print(count_evens(-5, 5))