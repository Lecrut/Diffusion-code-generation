def add_to_list(input_list: list[int], add_item: int) -> list[int]:
    result = [x + add_item for x in input_list]
    return result

if __name__ == '__main__':
    area = [1, 5, 10, 15]
    value = 7
    output = add_to_list(area, value)
    print(output)