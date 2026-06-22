def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c'],
        [10, 20],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for s in sample_lists:
        print(get_penultimate(s))
    try:
        get_penultimate([1])
    except ValueError as e:
        print(e)
    try:
        get_penultimate([])
    except ValueError as e:
        print(e)