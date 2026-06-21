def contains_item(lst, value):
    return value in set(lst)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(contains_item(sample_list, 3))
    print(contains_item(sample_list, 6))