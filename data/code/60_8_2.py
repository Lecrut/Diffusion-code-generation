if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    last_element_slicing = my_list[-1]
    last_element_indexing = my_list[-1]
    print(f"List: {my_list}")
    print(f"Last element via slicing: {last_element_slicing}")
    print(f"Last element via indexing: {last_element_indexing}")
    best_practice = my_list[-1]
    print(f"Most efficient/Pythonic way: {best_practice}")