def get_middle(lst):
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
        [1, 3, 5],
        [1, 2, 3, 4],
        [10, 20, 30, 40, 50],
        [1],
        [1, 2]
    ]
    for arr in samples:
        result = get_middle(arr)
        print(result)