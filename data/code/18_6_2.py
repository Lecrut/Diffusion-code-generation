def find_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    for sample in sample_lists:
        result = find_middle_element(sample)
        print(result)