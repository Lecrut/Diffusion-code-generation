def find_middle(sequence):
    middle_index = len(sequence) // 2
    return sequence[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple1 = (10, 20, 30, 40, 50)
    list2 = ['a', 'b', 'c']
    tuple2 = ('x', 'y', 'z')
    list3 = [100]
    tuple3 = (200,)
    print(find_middle(list1))
    print(find_middle(tuple1))
    print(find_middle(list2))
    print(find_middle(tuple2))
    print(find_middle(list3))
    print(find_middle(tuple3))