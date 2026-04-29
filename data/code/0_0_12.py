def add_item_efficiently(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    input_list = [1, 2, 3]
    input_item = 4

    output = add_item_efficiently(input_list, input_item)

    print(output)