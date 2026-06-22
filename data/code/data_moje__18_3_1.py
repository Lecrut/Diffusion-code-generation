def get_central_element(lst):
    if not lst:
        raise ValueError("List is empty")
    index = len(lst) // 2
    return lst[index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [100],
        [1, 2],
        [5, 6, 7, 8, 9, 10]
    ]
    for sample in sample_lists:
        result = get_central_element(sample)
        print(result)