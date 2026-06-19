def get_first_element(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_first_element(sample_list))