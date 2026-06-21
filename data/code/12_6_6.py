def get_center_element(collection):
    if not collection:
        return None
    length = len(collection)
    if length % 2 == 1:
        return collection[length // 2]
    else:
        return (collection[length // 2 - 1], collection[length // 2])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30, 40)
    sample_odd_tuple = (1, 2, 3)
    empty_list = []
    
    print(get_center_element(sample_list))
    print(get_center_element(sample_tuple))
    print(get_center_element(sample_odd_tuple))
    print(get_center_element(empty_list))