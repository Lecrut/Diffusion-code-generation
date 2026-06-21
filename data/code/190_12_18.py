def check_item_existence(item_list):
    item_set = set(item_list)

    def exists(item):
        return item in item_set
    return exists
if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    item_checker = check_item_existence(sample_items)
    print(item_checker('banana'))
    print(item_checker('grape'))