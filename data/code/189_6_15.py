ITEMS_TO_REMOVE = {2, 4, 6}

def remove_items_from_list(original_list):
    return [item for item in original_list if item not in ITEMS_TO_REMOVE]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    result = remove_items_from_list(sample_list)
    print(result)