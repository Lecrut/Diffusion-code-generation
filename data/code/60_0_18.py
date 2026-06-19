def find_last_element(data):
    if not data:
        return None
    return data[-1]

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    last_item = find_last_element(example_list)
    print(last_item)