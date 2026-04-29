def append_item(data: list, item: object) -> None:
    data.append(item)

if __name__ == '__main__':
    input_list = [1, 2, 3]
    item_to_add = 4

    print(input_list)

    append_item(input_list, item_to_add)

    print(input_list)

    input_list_two = ['a', 'b']
    item_two = 'c'

    print(input_list_two)

    append_item(input_list_two, item_two)

    print(input_list_two)