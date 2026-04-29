def add_to_end(input_list: list, item: object) -> list:
    input_list.append(item)
    return input_list

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    item_to_add = 4

    result_list = add_to_end(initial_list, item_to_add)

    print(result_list)