def is_valid_index(lst, index):
    return 0 <= index < len(lst)

def pop_element_from_list(lst, index):
    if not is_valid_index(lst, index):
        print("Error: Index out of bounds.")
        return None
    element = lst.pop(index)
    return element

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    removed_element = pop_element_from_list(my_list, index_to_pop)
    if removed_element is not None:
        print(f"Element removed: {removed_element}")
        print(f"List after pop: {my_list}")