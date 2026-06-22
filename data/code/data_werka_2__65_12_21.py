def get_element_by_index(lst, index):
    if index < -len(lst) or index >= len(lst):
        raise IndexError('Index out of bounds')
    return lst[index]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    positive_index = 3
    negative_index = -2
    out_of_bounds_positive = 5
    out_of_bounds_negative = -6

    print(f"Element at index {positive_index}: {get_element_by_index(sample_list, positive_index)}")
    print(f"Element at index {negative_index}: {get_element_by_index(sample_list, negative_index)}")

    try:
        print(f"Element at index {out_of_bounds_positive}: {get_element_by_index(sample_list, out_of_bounds_positive)}")
    except IndexError as e:
        print(e)

    try:
        print(f"Element at index {out_of_bounds_negative}: {get_element_by_index(sample_list, out_of_bounds_negative)}")
    except IndexError as e:
        print(e)