def get_first_item(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_first_item(sample_list))