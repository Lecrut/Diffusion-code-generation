if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    last_element_slice = my_list[-1]
    last_element_index = len(my_list) - 1
    last_element_index_access = my_list[last_element_index]
    print(f"List: {my_list}")
    print(f"Slicing access ([-1]): {last_element_slice}")
    print(f"Indexing access ([-1]): {my_list[-1]}")
    print(f"Indexing access (len-1): {my_list[len(my_list) - 1]}")
    most_efficient_access = my_list[-1]
    print(f"Most efficient Pythonic access: {most_efficient_access}")