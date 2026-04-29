def add_item_to_list(input_list: list, item_to_add: int) -> list:
    result = [x + item_to_add for x in input_list]
    return result

if __name__ == '__main__':
    area = [1, 5, 10, 15]
    value = 7
    output = add_item_to_list(area, value)
    print(output)