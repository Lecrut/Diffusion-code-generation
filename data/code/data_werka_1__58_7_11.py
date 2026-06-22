def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = ['x', 'y', 'z']
    empty_sample = []
    single_element_list = [45]

    print(f"First element of {sample_list1}: {get_first_element(sample_list1)}")
    print(f"First element of {sample_list2}: {get_first_element(sample_list2)}")
    print(f"First element of {empty_sample}: {get_first_element(empty_sample)}")
    print(f"First element of {single_element_list}: {get_first_element(single_element_list)}")