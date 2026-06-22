def get_second_element(lst):
    if len(lst) < 2:
        raise IndexError("List does not contain at least two elements.")
    return lst[1]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    try:
        print(get_second_element(my_list))
    except IndexError as e:
        print(e)