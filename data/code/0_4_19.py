def add_to_list(input_list: list[int], add_value: int) -> list[int]:
    result = [x + add_value for x in input_list]
    return result

if __name__ == '__main__':
    area = [1, 2, 3, 4, 5]
    value = 10
    output = add_to_list(area, value)
    print(output)