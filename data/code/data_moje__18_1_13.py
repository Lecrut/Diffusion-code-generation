def get_median(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    return sorted_list[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 3, 5, 7, 9],
        [10, 20, 30, 40],
        [42],
        []
    ]
    for case in test_cases:
        print(get_median(case))