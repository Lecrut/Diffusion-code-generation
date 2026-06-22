def count_evens(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    if start > end:
        return 0
    count = (end // 2) - ((start - 1) // 2)
    return count

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(4, 4))
    print(count_evens(5, 5))
    print(count_evens(10, 20))
    print(count_evens(21, 30))