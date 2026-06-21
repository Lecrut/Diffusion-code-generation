def item_exists(item_list, target):
    return target in item_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(item_exists(sample_list, 3))
    print(item_exists(sample_list, 6))