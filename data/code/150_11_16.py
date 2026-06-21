ITEM_TO_REMOVE = 3

def remove_item_from_list(input_list):
    return [item for item in input_list if item != ITEM_TO_REMOVE]
if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 3]
    filtered_list = remove_item_from_list(original_list)
    print(f'Original list: {original_list}')
    print(f'Item to remove: {ITEM_TO_REMOVE}')
    print(f'New list: {filtered_list}')