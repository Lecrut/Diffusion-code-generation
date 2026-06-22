def get_middle_element(lst):
    length = len(lst)
    if length == 0:
        return None
    index = length // 2
    return lst[index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        [10, 20, 30, 40],
        [100],
        [5, 15, 25, 35, 45, 55, 65]
    ]
    for lst in sample_lists:
        result = get_middle_element(lst)
        print(result)