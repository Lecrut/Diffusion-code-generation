def get_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    lists = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
    for l in lists:
        result = get_middle_element(l)
        print(result)