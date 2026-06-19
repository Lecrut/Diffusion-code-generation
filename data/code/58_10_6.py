def get_first_element(some_list):
    if not some_list:
        return None
    return some_list[0]

if __name__ == '__main__':
    test_list = [5, 10, 15, 20]
    print(get_first_element(test_list))