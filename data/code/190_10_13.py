def contains_item(data_list: list, target_item) -> bool:
    return target_item in data_list

if __name__ == '__main__':
    sample_list = [1, 5, 9, 12, 3]
    target_value = 9
    result = contains_item(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}, Result: {result}")