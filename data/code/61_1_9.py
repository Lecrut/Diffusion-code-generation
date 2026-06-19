def get_element_at_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Index out of range'
    except TypeError:
        return 'Invalid list or index type'
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_at_position(sample_list, 2))
    print(get_element_at_position(sample_list, 5))
    print(get_element_at_position('not a list', 1))