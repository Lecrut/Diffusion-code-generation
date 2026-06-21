def is_item_in_list(item: int, master_list: list) -> bool:
    return item in master_list
if __name__ == '__main__':
    target = 5
    master = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = is_item_in_list(target, master)
    print(result)