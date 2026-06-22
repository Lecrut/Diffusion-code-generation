def retrieve_first_element(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    print(retrieve_first_element(test_list))