def get_median(sorted_list):
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

if __name__ == '__main__':
    test_cases = [
        [1, 3, 5],
        [1, 2, 3, 4],
        [10],
        [5, 10],
        [1, 2, 3, 4, 5, 6, 7]
    ]
    for case in test_cases:
        print(get_median(case))