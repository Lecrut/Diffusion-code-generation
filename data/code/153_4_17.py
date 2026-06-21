def item_exists(item_list: list, search_item: int) -> bool:
    return search_item in item_list

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    search_value = 30
    result = item_exists(sample_list, search_value)
    print(result)