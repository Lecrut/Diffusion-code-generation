def find_largest_in_range(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return end

if __name__ == '__main__':
    print(find_largest_in_range(5, 10))
    print(find_largest_in_range(-10, -5))
    print(find_largest_in_range(0, 0))