def min_in_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Inputs must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return min(range(start, end + 1))

if __name__ == '__main__':
    try:
        print(min_in_range(5, 10))
    except ValueError as e:
        print(e)