def contains_item(data_list: list, target_item) -> bool:
    if not isinstance(data_list, list):
        raise ValueError("data_list must be a list")
    return target_item in data_list

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    target_value = 8
    result = contains_item(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}, Result: {result}")

    sample_list = ['a', 'b', 'c', 'd']
    target_value = 'e'
    result = contains_item(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}, Result: {result}")

    sample_list = [1000000, 2000000]
    target_value = 1000000
    result = contains_item(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}, Result: {result}")