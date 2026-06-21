def get_last_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_element(sample_list))

    single_element_list = [42]
    print(get_last_element(single_element_list))

    string_list = ['apple', 'banana', 'cherry']
    print(get_last_element(string_list))