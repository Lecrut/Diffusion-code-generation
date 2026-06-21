def remove_duplicates_by_item(input_list, item_to_remove):
    if not isinstance(input_list, list) or not all(isinstance(x, (list, tuple)) for x in input_list):
        raise ValueError("Input must be a list of lists or tuples")
    
    return [item for item in input_list if item != item_to_remove]

if __name__ == '__main__':
    sample_list = [[1, 'a'], [2, 'b'], [3, 'a'], [4, 'c'], [5, 'a']]
    item_to_exclude = [3, 'a']
    result_list = remove_duplicates_by_item(sample_list, item_to_exclude)
    print(result_list)