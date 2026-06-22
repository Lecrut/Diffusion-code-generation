def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_lists = [[1, 2, 3, 4], ['a', 'b', 'c'], [10, 20]]
    for lst in sample_lists:
        print(get_penultimate(lst))

    try:
        get_penultimate([1])
    except ValueError as e:
        print(e)

    try:
        get_penultimate([])
    except ValueError as e:
        print(e)