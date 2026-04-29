def add_to_list(data: list, item: object) -> list:
    data.append(item)
    return data

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    new_item = 40
    result = add_to_list(initial_list, new_item)
    print(result)