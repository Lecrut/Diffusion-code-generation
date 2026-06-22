def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    samples = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [42],
        [],
        [7, 8, 9, 10, 11, 12, 13]
    ]
    for sample in samples:
        result = get_middle_element(sample)
        print(result)