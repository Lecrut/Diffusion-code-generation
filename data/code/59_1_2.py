def find_middle_item(sequence):
    middle_index = len(sequence) // 2
    return sequence[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple1 = (10, 20, 30, 40, 50)
    list2 = ['a', 'b', 'c']
    tuple2 = ('x', 'y', 'z')
    list3 = [100]
    tuple3 = (200,)
    print(find_middle_item(list1))
    print(find_middle_item(tuple1))
    print(find_middle_item(list2))
    print(find_middle_item(tuple2))
    print(find_middle_item(list3))
    print(find_middle_item(tuple3))