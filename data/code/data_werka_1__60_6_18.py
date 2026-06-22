def get_last_element(safe_list):
    try:
        return safe_list[-1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    empty_data = []
    single_element_data = [42]
    print('Last element of sample_data:', get_last_element(sample_data))
    print('Last element of empty_data:', get_last_element(empty_data))
    print('Last element of single_element_data:', get_last_element(single_element_data))