def count_evens(start, end):
    if start > end:
        start, end = end, start
    first_even = start if start % 2 == 0 else start + 1
    if first_even > end:
        return 0
    return (end - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(3, 9))
    print(count_evens(2, 2))
    print(count_evens(1, 1))
    print(count_evens(5, 5))