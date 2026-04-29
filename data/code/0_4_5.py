def add_item_to_list(data: list[int], item: int) -> list[int]:
    result = [x + item for x in data]
    return result

if __name__ == '__main__':
    area = [1, 5, 10, 15]
    value = 7
    output = add_item_to_list(area, value)