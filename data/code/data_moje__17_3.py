def get_last_element(collection):
    if not collection:
        raise IndexError("collection is empty")
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    print(get_last_element(sample_list))
    print(get_last_element(sample_tuple))