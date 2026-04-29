def add_item_to_list(list_in: list, item_to_add: int) -> list:
    return [x + item_to_add for x in list_in]

if __name__ == '__main__':
    area = [1, 2, 3, 4]
    value = 10
    output = add_item_to_list(area, value)
    print(output)