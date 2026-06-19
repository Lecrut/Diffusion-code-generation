MIDDLE_INDEX_CONSTANT = 2

def find_middle(sequence):
    middle_index = len(sequence) // MIDDLE_INDEX_CONSTANT
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_tuple_1 = (10, 20, 30, 40, 50)
    sample_list_2 = ['x', 'y', 'z']
    sample_tuple_2 = ('a', 'b', 'c')
    sample_list_3 = [100]
    sample_tuple_3 = (200,)
    
    print(find_middle(sample_list_1))
    print(find_middle(sample_tuple_1))
    print(find_middle(sample_list_2))
    print(find_middle(sample_tuple_2))
    print(find_middle(sample_list_3))
    print(find_middle(sample_tuple_3))