def sum_range(start: int, end: int) -> int:
    if start > end:
        raise ValueError('Start value must be less than or equal to end value')
    return (end - start + 1) * (start + end) // 2
if __name__ == '__main__':
    try:
        print(sum_range(1, 10))
        print(sum_range(5, 15))
        print(sum_range(3, 9))
        print(sum_range(15, 5))
    except ValueError as e:
        print(e)