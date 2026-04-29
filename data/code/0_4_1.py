def add_item_to_list(list_in: list[int], item_to_add: int) -> list[int]:
    result = [x + item_to_add for x in list_in]
    return result

if __name__ == '__main__':
    list_in = [1, 5, 10, 15]
    item_to_add = 7
    output = add_item_to_list(list_in, item_to_add)
    print(output)