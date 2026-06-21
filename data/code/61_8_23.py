def pop_element_from_list(lst, index):
    try:
        return lst.pop(index)
    except IndexError:
        raise ValueError("Index out of range")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    try:
        removed_element = pop_element_from_list(sample_list, index_to_pop)
        print(f"Removed element: {removed_element}")
        print(f"List after removal: {sample_list}")
    except ValueError as e:
        print(e)