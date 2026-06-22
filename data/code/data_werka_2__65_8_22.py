def get_element_by_position(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    if index < 0 or index >= len(lst):
        raise IndexError(f"Index {index} is out of bounds for the given list.")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_by_position(sample_list, 2))
    except IndexError as e:
        print(e)
    try:
        print(get_element_by_position(sample_list, 5))
    except IndexError as e:
        print(e)