def get_element_at_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid input type"

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    print(get_element_at_position(sample_list, index_to_access))