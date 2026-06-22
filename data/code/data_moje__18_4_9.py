def get_middle_value(lst):
    n = len(lst)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 1:
        return lst[mid_index]
    else:
        return (lst[mid_index - 1] + lst[mid_index]) / 2

if __name__ == '__main__':
    samples = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [5],
        [10, 20],
        [1, 3, 5, 7, 9],
        [],
        [42]
    ]
    for s in samples:
        print(get_middle_value(s))