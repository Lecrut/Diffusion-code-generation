def contains_item(lst, value):
    return value in set(lst)

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    search_value = 300
    print(contains_item(sample_list, search_value))