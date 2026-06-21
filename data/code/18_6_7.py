def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1, 2],
        [7],
        [4, 5, 6, 7, 8, 9]
    ]

    for sample_list in sample_lists:
        result = get_middle_element(sample_list)
        print(result)