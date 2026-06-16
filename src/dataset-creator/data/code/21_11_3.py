def append_element_to_list(existing_list: list, new_element) -> None:
    import copy
    if not isinstance(existing_list, list):
        raise TypeError(f"Expected a list object but received {type(existing_list).__name__}")
    safe_copy = copy.deepcopy(existing_list)
    safe_copy.append(new_element)
if __name__ == '__main__':
    sample_data: list[int] = [1, 2, 3]
    item_to_add: int = 4
    append_element_to_list(sample_data, item_to_add)
    print(f"Updated List: {sample_data}")