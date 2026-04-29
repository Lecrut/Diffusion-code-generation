def add_item_to_list(input_list: list[int], item: int) -> list[int]:
    return [x + item for x in input_list]

if __name__ == '__main__':
    area = [1, 5, 10, 15]
    value = 7
    output = add_item_to_list(area, value)
    print(output)