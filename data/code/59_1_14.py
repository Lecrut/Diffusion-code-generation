def find_middle(sequence):
    length = len(sequence)
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20, 25]
    sample_tuple1 = (100, 200, 300, 400, 500)
    sample_list2 = ['x', 'y', 'z']
    sample_tuple2 = ('apple', 'banana', 'cherry')
    sample_list3 = [7]
    sample_tuple3 = (42,)
    
    print(find_middle(sample_list1))
    print(find_middle(sample_tuple1))
    print(find_middle(sample_list2))
    print(find_middle(sample_tuple2))
    print(find_middle(sample_list3))
    print(find_middle(sample_tuple3))