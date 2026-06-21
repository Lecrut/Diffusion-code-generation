def check_item_exists(item: int, items_list: list[int]) -> bool:
    return item in set(items_list)

if __name__ == '__main__':
    target = 5
    master = list(range(1, 100))
    result = check_item_exists(target, master)
    print(result)