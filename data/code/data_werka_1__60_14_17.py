def fetch_last_element(array):
    if not isinstance(array, list):
        raise ValueError('Input must be a list')
    if len(array) == 0:
        return None
    return array[-1]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(fetch_last_element(sample_data))
    empty_list = []
    print(fetch_last_element(empty_list))
    single_element_list = [42]
    print(fetch_last_element(single_element_list))