def remove_element_at_index(lst, index):
    try:
        removed_element = lst.pop(index)
        return removed_element
    except IndexError:
        print('IndexError: Index out of range')
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_remove = 2
    removed_element = remove_element_at_index(sample_list, index_to_remove)
    if removed_element is not None:
        print(f'Removed element: {removed_element}')
        print(f'Updated list: {sample_list}')
    else:
        print('Failed to remove element.')