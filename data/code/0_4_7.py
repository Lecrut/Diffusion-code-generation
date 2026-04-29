def add_value_to_list(input_list: list[int], value: int) -> list[int]:
    return [x + value for x in input_list]

if __name__ == '__main__':
    area = [1, 2, 3, 4]
    value = 10
    output = add_value_to_list(area, value)
    print(output)