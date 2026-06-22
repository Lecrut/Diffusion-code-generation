def safe_pop(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    if index < 0 or index >= len(lst):
        return None
    return lst.pop(index)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    popped_element = safe_pop(sample_list, index_to_pop)
    if popped_element is not None:
        print("Popped element:", popped_element)
        print("Remaining list:", sample_list)
    else:
        print("Error: Index out of bounds.")