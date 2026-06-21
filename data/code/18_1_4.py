def get_median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        raise ValueError("List must not be empty")
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_list[mid_index]
    else:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2.0

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [10],
        [1, 3],
        [1, 2, 3]
    ]

    for tc in test_cases:
        sorted_tc = sorted(tc)
        median = get_median(sorted_tc)
        print(median)