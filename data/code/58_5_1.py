def count_evens_in_range(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    if first_even > end:
        return 0
    count = (end - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    print(count_evens_in_range(1, 10))
    print(count_evens_in_range(2, 2))
    print(count_evens_in_range(3, 3))
    print(count_evens_in_range(-5, 5))
    print(count_evens_in_range(10, 1))