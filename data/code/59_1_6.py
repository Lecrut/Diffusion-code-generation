def find_middle(sequence):
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_list2 = ['x', 'y', 'z']
    sample_tuple2 = ('a', 'b', 'c')
    sample_list3 = [100]
    sample_tuple3 = (200,)
    
    print(find_middle(sample_list1))
    print(find_middle(sample_tuple1))
    print(find_middle(sample_list2))
    print(find_middle(sample_tuple2))
    print(find_middle(sample_list3))
    print(find_middle(sample_tuple3))