def count_elements(sequence):
    return len(sequence)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c')
    empty_list = []
    single_element_tuple = (10,)
    print(f"Count for {list1}: {count_elements(list1)}")
    print(f"Count for {tuple2}: {count_elements(tuple2)}")
    print(f"Count for {empty_list}: {count_elements(empty_list)}")
    print(f"Count for {single_element_tuple}: {count_elements(single_element_tuple)}")