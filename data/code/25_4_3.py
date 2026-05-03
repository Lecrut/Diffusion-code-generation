def check_for_zero(data):
    for item in data:
        if item == 0:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 0, 3, 4]
    list3 = [5, 6, 7, 8]
    list4 = [0, 1, 2, 3]
    empty_list = []
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(empty_list)