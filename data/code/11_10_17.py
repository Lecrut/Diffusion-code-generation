def retrieve_last_entry(collection):
    offset = -1
    target_index = offset
    element = collection[target_index]
    return element

if __name__ == '__main__':
    data_set = [77, 88, 99, 110]
    final_item = retrieve_last_entry(data_set)
    print(final_item)