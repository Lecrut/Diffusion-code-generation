def contains_item(lst, value):
    return value in set(lst)

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10]
    search_value = 9
    print(contains_item(sample_list, search_value))