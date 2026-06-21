def remove_duplicates_by_item(input_list, item_to_remove):
    seen_items = set()
    output_list = []
    for element in input_list:
        if element not in seen_items:
            seen_items.add(element)
            output_list.append(element)
    return output_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    item_to_remove = 3
    result_list = remove_duplicates_by_item(sample_list, item_to_remove)
    print(result_list)