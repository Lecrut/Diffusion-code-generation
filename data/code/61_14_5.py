def get_element(sequence, index):
    return sequence[index]
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    my_tuple = (5, 15, 25, 35)
    index_to_find = 2
    list_element = get_element(my_list, index_to_find)
    print(f"Element at index {index_to_find} in the list {my_list}: {list_element}")
    tuple_element = get_element(my_tuple, index_to_find)
    print(f"Element at index {index_to_find} in the tuple {my_tuple}: {tuple_element}")