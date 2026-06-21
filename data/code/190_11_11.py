def contains_item(lst, item):
    return item in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_item = 3
    print(contains_item(sample_list, target_item))