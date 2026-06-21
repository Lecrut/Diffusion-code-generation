def get_penultimate(lst):
    if lst is None or len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10],
        [],
        [1, 2]
    ]
    for s in sample_lists:
        print(get_penultimate(s))