def find_median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

if __name__ == '__main__':
    test_cases = [
        [1, 3, 5],
        [1, 2, 3, 4],
        [10],
        [1, 2, 3, 4, 5, 6],
        [5, 15, 25]
    ]
    for case in test_cases:
        result = find_median(case)
        print(result)