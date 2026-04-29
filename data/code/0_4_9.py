def add_item_to_list(list_in: list, add_item: int) -> list:
    return [x + add_item for x in list_in]

if __name__ == '__main__':
    area = [1, 2, 3, 4, 5]
    value = 10
    output = add_item_to_list(area, value)
    print(output)