def get_first_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    my_list = [100, 200, 300]
    first = get_first_element(my_list)
    print(first)