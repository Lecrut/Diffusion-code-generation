def get_second_item(lst):
    if len(lst) < 2:
        raise IndexError("List does not have a second item.")
    return lst[1]

if __name__ == '__main__':
    sample_list = [9, 19, 29]
    try:
        second_value = get_second_item(sample_list)
        print(second_value)
    except IndexError as e:
        print(e)