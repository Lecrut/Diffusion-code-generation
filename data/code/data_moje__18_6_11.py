def get_middle(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    lists = [[1, 2, 3], [1, 2, 3, 4, 5], [10, 20, 30, 40]]
    for l in lists:
        print(get_middle(l))