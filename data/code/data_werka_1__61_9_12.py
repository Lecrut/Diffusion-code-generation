def pop_element_from_list(my_list, index):
    try:
        removed_element = my_list.pop(index)
        return removed_element
    except IndexError:
        print('Error: Index out of range')
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    result = pop_element_from_list(sample_list, index_to_pop)
    print('Removed element:', result)
    print('Updated list:', sample_list)