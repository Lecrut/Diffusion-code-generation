def remove_duplicates(data, item):
    if not isinstance(data, list) or not all(isinstance(x, (int, str)) for x in data):
        raise ValueError("Data must be a list of integers and/or strings.")
    if not isinstance(item, (int, str)):
        raise ValueError("Item to remove must be an integer or string.")
    
    return list(set(data) - {item})

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 2, 3]
    item_to_remove = 3
    result_list = remove_duplicates(input_list, item_to_remove)
    print(result_list)