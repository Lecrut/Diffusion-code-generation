def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    sample_lists = [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c']
    ]
    for sample in sample_lists:
        result = get_penultimate(sample)
        print(result)