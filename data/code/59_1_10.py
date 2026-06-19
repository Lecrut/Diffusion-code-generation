def find_middle(sequence):
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20, 25]
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_list2 = ['apple', 'banana', 'cherry']
    sample_tuple2 = ('dog', 'elephant', 'frog')
    sample_list3 = [99]
    sample_tuple3 = (88,)
    
    print(find_middle(sample_list1))
    print(find_middle(sample_tuple1))
    print(find_middle(sample_list2))
    print(find_middle(sample_tuple2))
    print(find_middle(sample_list3))
    print(find_middle(sample_tuple3))