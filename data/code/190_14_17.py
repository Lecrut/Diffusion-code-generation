def contains_item(lst, value):
    return value in set(lst)

if __name__ == '__main__':
    sample_list = ['red', 'green', 'blue', 'yellow']
    search_value = 'green'
    result = contains_item(sample_list, search_value)
    print(result)