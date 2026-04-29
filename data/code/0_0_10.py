def add_item_to_list(data_list: list, item) -> list:
    result = data_list
    result.append(item)
    return result

if __name__ == '__main__':
    input_list = [1, 2, 3]
    input_item = 4

    output = add_item_to_list(input_list, input_item)

    print(output)