def find_middle(sequence):
    MIDDLE_INDEX = len(sequence) // 2
    return sequence[MIDDLE_INDEX]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 2, 3, 4, 5]
    SAMPLE_TUPLE_1 = (10, 20, 30, 40, 50)
    SAMPLE_LIST_2 = ['a', 'b', 'c']
    SAMPLE_TUPLE_2 = ('x', 'y', 'z')
    SAMPLE_LIST_3 = [100]
    SAMPLE_TUPLE_3 = (200,)
    
    print(find_middle(SAMPLE_LIST_1))
    print(find_middle(SAMPLE_TUPLE_1))
    print(find_middle(SAMPLE_LIST_2))
    print(find_middle(SAMPLE_TUPLE_2))
    print(find_middle(SAMPLE_LIST_3))
    print(find_middle(SAMPLE_TUPLE_3))