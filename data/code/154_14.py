def count_elements(sequence):
    return len(sequence)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c')
    empty_list = []
    single_element = [100]
    print(f"Count of elements in {list1}: {count_elements(list1)}")
    print(f"Count of elements in {tuple2}: {count_elements(tuple2)}")
    print(f"Count of elements in {empty_list}: {count_elements(empty_list)}")
    print(f"Count of elements in {single_element}: {count_elements(single_element)}")