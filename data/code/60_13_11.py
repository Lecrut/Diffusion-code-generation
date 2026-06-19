def get_last_item(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    example_list = [7, 14, 21, 28, 35]
    last_element = get_last_item(example_list)
    print(last_element)