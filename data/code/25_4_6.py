def check_for_zero(data):
    for item in data:
        if item == 0:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 0, 3, 4, 5]
    list3 = [10, 20, 30]
    list4 = [0, 5, 10]
    list5 = []
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)