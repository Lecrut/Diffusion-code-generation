def get_second_element(data):
    return data[1] if len(data) > 1 else None

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    second_element = get_second_element(my_list)
    print(second_element)