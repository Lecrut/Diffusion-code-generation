def contains_item(data_list: list, target_item) -> bool:
    return target_item in set(data_list)

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    search_item = 8
    result = contains_item(sample_list, search_item)
    print(f"List: {sample_list}, Target: {search_item}, Result: {result}")