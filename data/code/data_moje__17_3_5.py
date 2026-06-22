def get_last_element(collection):
    if len(collection) == 0:
        raise IndexError("Cannot get the last element of an empty collection")
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_string = "Hello World"
    sample_tuple = (1, 2, 3, 4, 5)
    print(get_last_element(sample_list))
    print(get_last_element(sample_string))
    print(get_last_element(sample_tuple))