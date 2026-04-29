def add_to_end(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    new_item = 4
    result = add_to_end(initial_list, new_item)
    print(result)

    initial_list_2 = ['a', 'b']
    new_item_2 = 'c'
    result_2 = add_to_end(initial_list_2, new_item_2)
    print(result_2)