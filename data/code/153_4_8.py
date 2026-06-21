def check_item_existence(target_list: list, master_list: list) -> bool:
    return any(item in master_list for item in target_list)

if __name__ == '__main__':
    target = [1, 5, 9, 12]
    master = list(range(1, 100))
    result = check_item_existence(target, master)
    print(result)