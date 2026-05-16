def count_elements(sequence):
    return len(sequence)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c', 'd')
    empty_list = []
    single_element = [100]
    empty_tuple = ()
    print(f"Count of {list1}: {count_elements(list1)}")
    print(f"Count of {tuple2}: {count_elements(tuple2)}")
    print(f"Count of {empty_list}: {count_elements(empty_list)}")
    print(f"Count of {single_element}: {count_elements(single_element)}")
    print(f"Count of {empty_tuple}: {count_elements(empty_tuple)}")