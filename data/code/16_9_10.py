def get_first_element(int_list):
    if not int_list:
        return None
    return int_list[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    empty_list = []
    print(get_first_element(sample_list))
    print(get_first_element(empty_list))