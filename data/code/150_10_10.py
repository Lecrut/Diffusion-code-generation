def remove_element(lst, item_to_remove):
    return [x for x in lst if x != item_to_remove]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    item_to_remove = 'banana'
    result = remove_element(sample_list, item_to_remove)
    print(result)