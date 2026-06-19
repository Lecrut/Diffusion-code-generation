def get_second_item(lst):
    if len(lst) < 2:
        raise IndexError("List must contain at least two elements.")
    return lst[1]

if __name__ == '__main__':
    sample_list = [4, 14, 24]
    try:
        second_element = get_second_item(sample_list)
        print(second_element)
    except IndexError as e:
        print(e)