def get_last_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_element(sample_list))
    sample_list2 = ['apple', 'banana', 'cherry']
    print(get_last_element(sample_list2))
    single_element_list = [42]
    print(get_last_element(single_element_list))