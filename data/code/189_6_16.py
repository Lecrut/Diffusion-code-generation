def remove_items_from_list(items_to_remove, original_list):
    items_set = set(items_to_remove)
    return [item for item in original_list if item not in items_set]
if __name__ == '__main__':
    sample_items_to_remove = ['apple', 'banana']
    sample_original_list = ['apple', 'orange', 'banana', 'grape']
    result = remove_items_from_list(sample_items_to_remove, sample_original_list)
    print(result)