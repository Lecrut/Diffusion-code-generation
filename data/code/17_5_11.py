def get_last_element(sequence):
    return sequence[-1]

if __name__ == '__main__':
    categories = {'x': 10, 'y': 20, 'z': 30}
    data_list = list(categories.values())
    print(get_last_element(data_list))