def check_item_existence(item_list):
    item_set = set(item_list)

    def exists(item):
        return item in item_set
    return exists
if __name__ == '__main__':
    sample_items = [1, 2, 3, 4, 5]
    checker = check_item_existence(sample_items)
    print(checker(3))
    print(checker(6))