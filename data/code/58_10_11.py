def retrieve_first_element():
    my_list = [5, 10, 15, 20, 25]
    first_item = my_list[0] if my_list else None
    return first_item

if __name__ == '__main__':
    sample_sequence = [3, 6, 9, 12]
    print(retrieve_first_element())