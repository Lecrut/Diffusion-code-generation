def contains_item(lst, value):
    item_set = set(lst)
    return value in item_set

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'orange']
    search_value = 'banana'
    result = contains_item(sample_list, search_value)
    print(result)