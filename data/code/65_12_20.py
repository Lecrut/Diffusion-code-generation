MIN_INDEX = -100
MAX_INDEX = 100

def get_element_by_index(lst, index):
    if not (MIN_INDEX <= index < len(lst) or -len(lst) <= index <= MAX_INDEX):
        raise IndexError('Index out of bounds')
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_by_index(sample_list, 2))
    print(get_element_by_index(sample_list, -1))
    try:
        print(get_element_by_index(sample_list, 5))
    except IndexError as e:
        print(e)
    try:
        print(get_element_by_index(sample_list, -6))
    except IndexError as e:
        print(e)