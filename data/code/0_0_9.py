def add_to_list(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    input_list = [1, 2, 3]
    input_item = 4

    result = add_to_list(input_list, input_item)

    print(result)