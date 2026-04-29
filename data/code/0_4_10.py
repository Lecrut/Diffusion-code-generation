def add_item_to_list(data_list: list[int], item: int) -> list[int]:
    result = [x + item for x in data_list]
    return result

if __name__ == '__main__':
    area = [5, 10, 15, 20]
    value = 7
    output = add_item_to_list(area, value)
    print(output)