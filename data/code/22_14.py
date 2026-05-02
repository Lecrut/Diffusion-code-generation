def filter_odd_numbers(data):
    return [x for x in data if x % 2 != 0]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [2, 4, 6, 8, 10]
    list3 = [11, 22, 33, 44, 55]
    list4 = []
    list5 = [7, 9, 11]
    print(filter_odd_numbers(list1))
    print(filter_odd_numbers(list2))
    print(filter_odd_numbers(list3))
    print(filter_odd_numbers(list4))
    print(filter_odd_numbers(list5))