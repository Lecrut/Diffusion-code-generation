def get_final_item(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) == 0:
        return None
    return arr[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_final_item(sample_list))

    empty_list = []
    print(get_final_item(empty_list))

    single_element_list = ['hello']
    print(get_final_item(single_element_list))