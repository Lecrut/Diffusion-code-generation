def get_center_element(collection):
    length = len(collection)
    if length == 0:
        return None
    center_index = length // 2
    return collection[center_index]

if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (100, 200, 300)
    empty_list = []
    
    print(get_center_element(list_sample))
    print(get_center_element(tuple_sample))
    print(get_center_element(empty_list))