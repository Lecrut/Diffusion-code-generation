def count_evens(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_evens(3, 15))
    print(count_evens(2, 10))
    print(count_evens(5, 5))
    print(count_evens(4, 4))
    print(count_evens(10, 2))