def is_valid_index(index, lst):
    return 0 <= index < len(lst)

def pop_element_from_list(lst, index):
    if not is_valid_index(index, lst):
        print("Error: Index out of bounds.")
        return None
    return lst.pop(index)

if __name__ == '__main__':
    my_list = [5, 15, 25, 35, 45]
    index_to_pop = 3
    removed_element = pop_element_from_list(my_list, index_to_pop)
    if removed_element is not None:
        print(f"Element removed: {removed_element}")
        print(f"List after pop: {my_list}")