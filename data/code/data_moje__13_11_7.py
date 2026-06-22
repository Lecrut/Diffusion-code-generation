def get_tuple_element(t, index):
    if index < 0 or index >= len(t):
        return None
    return t[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    print(get_tuple_element(sample_tuple, 1))
    print(get_tuple_element(sample_tuple, 5))
    print(get_tuple_element(sample_tuple, 0))
    print(get_tuple_element(sample_tuple, -1))