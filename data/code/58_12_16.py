def count_evens(start: int, end: int) -> int:
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if start > end:
        return 0
    return (end - start) // 2 + 1
if __name__ == '__main__':
    start_val = 10
    end_val = 20
    result = count_evens(start_val, end_val)
    print(result)