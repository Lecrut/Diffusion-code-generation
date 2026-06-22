def find_middle(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list")
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [50],
        [100, 200]
    ]
    for lst in sample_lists:
        try:
            print(find_middle(lst))
        except ValueError as e:
            print(e)