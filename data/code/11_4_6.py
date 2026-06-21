def get_last_element(items):
    if not items:
        raise IndexError("list is empty")
    last_index = len(items) - 1
    return items[last_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_element(sample_list))