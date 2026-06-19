def get_second_element(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    print(get_second_element(my_list))