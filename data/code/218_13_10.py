def find_min_range(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return min(range(start, end + 1))

if __name__ == '__main__':
    print(find_min_range(5, 10))