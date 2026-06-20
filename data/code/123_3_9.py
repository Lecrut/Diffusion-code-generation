def sum_range(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    result = sum_range(1, 10)
    print(result)