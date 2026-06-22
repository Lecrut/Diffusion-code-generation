def count_evens_in_range(start, end):
    if start > end:
        return 0
    count = 0
    if start % 2 != 0:
        start += 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    print(count_evens_in_range(1, 10))
    print(count_evens_in_range(5, 5))
    print(count_evens_in_range(10, 1))
    print(count_evens_in_range(-5, 5))