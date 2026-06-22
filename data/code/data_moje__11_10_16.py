LAST_INDEX_OFFSET = -1

def get_last_element(input_list):
    return input_list[LAST_INDEX_OFFSET]

if __name__ == '__main__':
    my_data = [7, 3, 9, 1, 5]
    value = get_last_element(my_data)
    print(value)