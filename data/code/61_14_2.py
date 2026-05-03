def get_element(sequence, index):
    return sequence[index]
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    my_tuple = (5, 15, 25, 35)
    index_to_find = 2
    result_list = get_element(my_list, index_to_find)
    print(f"Element from list at index {index_to_find}: {result_list}")
    result_tuple = get_element(my_tuple, index_to_find)
    print(f"Element from tuple at index {index_to_find}: {result_tuple}")