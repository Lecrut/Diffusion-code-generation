def count_items(nested_list):
    item_count = 0
    for element in nested_list:
        if isinstance(element, list):
            item_count += count_items(element)
        else:
            item_count += 1
    return item_count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_items(sample_list))