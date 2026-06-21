LAST_ITEM_KEY = "last_element"

def get_last(lst):
    sliced = lst[-1:]
    value = sliced[0]
    return value

if __name__ == '__main__':
    data_list = [100, 200, 300, 400]
    result = get_last(data_list)
    print(result)
    lookup_map = {LAST_ITEM_KEY: get_last}
    retrieved = lookup_map[LAST_ITEM_KEY](data_list)
    print(retrieved)