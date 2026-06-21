def check_item_exists(item_list: list, target_item: int) -> bool:
    return target_item in item_list

if __name__ == '__main__':
    items = [10, 20, 30, 40, 50]
    search_for = 30
    result = check_item_exists(items, search_for)
    print(result)