def merge_tuples(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    LIST1 = [(1, 2), (3, 4)]
    LIST2 = [(5, 6), (7, 8)]
    result = merge_tuples(LIST1, LIST2)
    print(result)