def get_value_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        raise ValueError("Index is out of bounds")

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    result = get_value_at_index(my_list, 2)
    print(result)
    invalid_result = get_value_at_index(my_list, 10)
    print(invalid_result)