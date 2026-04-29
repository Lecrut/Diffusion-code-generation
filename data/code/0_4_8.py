def add_item_to_list(list_in: list, add_item: int) -> list:
    result = [x + add_item for x in list_in]
    return result

if __name__ == '__main__':
    list_data = [1, 5, 10, 15]
    add_value = 3
    output = add_item_to_list(list_data, add_value)
    print(output)