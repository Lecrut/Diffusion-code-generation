def contains_item(lst, value):
    return value in set(lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(contains_item(sample_list, 30))
    print(contains_item(sample_list, 60))