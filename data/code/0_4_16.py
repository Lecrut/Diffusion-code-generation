def add_to_list(list_in: list, add_item: int) -> list:
    result = [x + add_item for x in list_in]
    return result

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    item_b = 10
    output = add_to_list(list_a, item_b)
    print(output)