def remove_duplicates(input_list, item_to_remove):
    item_set = set(input_list)
    result = [item for item in item_set if item != item_to_remove]
    return result

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'apple', 'date']
    item_to_be_removed = 'apple'
    filtered_list = remove_duplicates(sample_list, item_to_be_removed)
    print(filtered_list)