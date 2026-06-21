def contains_item(lst, value):
    return value in set(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    search_value = 'banana'
    result = contains_item(sample_list, search_value)
    print(result)