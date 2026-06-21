def get_median(sorted_list):
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

if __name__ == '__main__':
    sample_lists = [
        [1, 3, 5],
        [1, 2, 3, 4],
        [10],
        [2, 2, 2, 2],
        []
    ]

    for sample in sample_lists:
        if sample:
            result = get_median(sample)
            print(result)
        else:
            print(None)