def item_exists_in_list(item, items):
    return item in set(items)

if __name__ == '__main__':
    target_item = 5
    sample_items = [1, 3, 5, 7, 9]
    result = item_exists_in_list(target_item, sample_items)
    print(f"Does {target_item} exist in {sample_items}? {result}")
    
    target_item = 2
    sample_items = [1, 3, 5, 7, 9]
    result = item_exists_in_list(target_item, sample_items)
    print(f"Does {target_item} exist in {sample_items}? {result}")
    
    target_item = 9
    sample_items = [9, 9, 9]
    result = item_exists_in_list(target_item, sample_items)
    print(f"Does {target_item} exist in {sample_items}? {result}")