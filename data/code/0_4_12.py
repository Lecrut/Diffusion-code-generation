def add_item_to_list(list_in: list[int], add_item: int) -> list[int]:
    result = [x + add_item for x in list_in]
    return result

if __name__ == '__main__':
    list_in = [1, 5, 10, 15]
    add_item = 7
    output = add_item_to_list(list_in, add_item)
    print(output)