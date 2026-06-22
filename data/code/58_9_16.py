def count_evens(start, end):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise TypeError("start and end must be numbers")
    if not isinstance(start, int):
        start = int(start)
    if not isinstance(end, int):
        end = int(end)
    if start > end:
        return 0
    count_to_end = end // 2
    count_to_start_minus_one = (start - 1) // 2
    return count_to_end - count_to_start_minus_one

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)
    result = count_evens(2, 20)
    print(result)
    result = count_evens(5, 5)
    print(result)
    result = count_evens(6, 6)
    print(result)
    result = count_evens(10, 5)
    print(result)