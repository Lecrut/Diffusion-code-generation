def filter_out_item(lst, item):
    return list(filter(lambda x: x != item, lst))

if __name__ == '__main__':
    original_list = [10, 20, 30, 40, 50]
    target_item = 30
    filtered_list = filter_out_item(original_list, target_item)
    print(f"Original list: {original_list}")
    print(f"Target item: {target_item}")
    print(f"Filtered list: {filtered_list}")