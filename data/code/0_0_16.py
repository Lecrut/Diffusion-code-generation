def add_item_to_list(data: list, item: int) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    input_list = [1, 2, 3]
    item_to_add = 4

    output_list = add_item_to_list(input_list, item_to_add)

    print(output_list)