def remove_element(lst, item_to_remove):
    return [x for x in lst if x != item_to_remove]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove = 3
    result = remove_element(sample_list, item_to_remove)
    print(result)