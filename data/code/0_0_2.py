def add_item_to_list(data_list: list, item: object) -> None:
    data_list.append(item)

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    new_item = 4

    print(initial_list)

    add_item_to_list(initial_list, new_item)

    print(initial_list)

    initial_list_two = ['a', 'b']
    new_item_two = 'c'

    print(initial_list_two)

    add_item_to_list(initial_list_two, new_item_two)

    print(initial_list_two)