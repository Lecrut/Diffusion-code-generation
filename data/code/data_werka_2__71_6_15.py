def find_median(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if len(data) == 0:
        return None
    sorted_data = sorted(data)
    count = len(sorted_data)
    if count % 2 == 1:
        return sorted_data[count // 2]
    return sorted_data[count // 2 - 1]

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40, 50],
        [5, 1, 9, 3, 7, 2],
        [42],
        [100, 200, 300, 400, 500, 600]
    ]
    for lst in sample_lists:
        result = find_median(lst)
        print(result)