def list_sum(iterable):
    return sum(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(list_sum(list1))
    list2 = [10, -5, 20.5, 0]
    print(list_sum(list2))
    list3 = []
    print(list_sum(list3))
    list4 = [100]
    print(list_sum(list4))