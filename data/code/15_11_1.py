def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_lists = [[1, 2, 3, 4, 5], [10, 20], ['a', 'b', 'c'], [42, 99]]
    for s in sample_lists:
        print(get_penultimate(s))