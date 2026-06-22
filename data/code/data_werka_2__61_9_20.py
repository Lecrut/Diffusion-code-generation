def get_element_from_list(lst, index):
    try:
        return lst[index]
    except IndexError:
        raise ValueError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_retrieve = 3
    try:
        element = get_element_from_list(sample_list, index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)