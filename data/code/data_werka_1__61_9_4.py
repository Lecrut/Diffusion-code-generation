def remove_element_at_index(lst, index):
    try:
        element = lst.pop(index)
        return element
    except IndexError:
        print("Index out of range")
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_remove = 2
    removed_element = remove_element_at_index(sample_list, index_to_remove)
    print("Removed element:", removed_element)
    print("Updated list:", sample_list)