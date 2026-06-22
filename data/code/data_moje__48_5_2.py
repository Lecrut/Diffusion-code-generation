def find_largest_across_lists():
    lists = [
        [1, 2, 3],
        [4, 5, 6, 7],
        [0, -1, -2],
        [10, 20]
    ]
    max_val = float('-inf')
    for lst in lists:
        for val in lst:
            if val > max_val:
                max_val = val
    return max_val

if __name__ == '__main__':
    result = find_largest_across_lists()
    print(result)