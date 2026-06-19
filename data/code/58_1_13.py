def get_first_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    example_list = [7, 14, 21, 28]
    print(get_first_element(example_list))