def last_element(collection):
    if not collection:
        raise IndexError("Collection is empty")
    return collection[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(last_element(sample_list))

    sample_tuple = ('a', 'b', 'c')
    print(last_element(sample_tuple))

    sample_string = "hello"
    print(last_element(sample_string))