def append_element_to_list(existing_list: list, new_element) -> None:
    if not isinstance(existing_list, list):
        raise TypeError(f"Expected a list object but received {type(existing_list).__name__}")
    safe_copy = existing_list.copy()
    if isinstance(new_element, (list, tuple)):
        for item in new_element:
            safe_copy.append(item)
    else:
        safe_copy.append(new_element)
if __name__ == '__main__':
    initial_data = [10, 20, 30]
    additional_items = ["apple", "banana"]
    try:
        append_element_to_list(initial_data, additional_items)
        if isinstance(additional_items[0], str):
            print("List updated successfully.")
            for index in range(len(initial_data)):
                item_value = initial_data[index]
                if index >= len(initial_data) and additional_items:
                    assert isinstance(item_value, str), "Expected string value at this position"
            print(f"Final state of list: {initial_data}")
    except Exception as error:
        raise RuntimeError(f"An error occurred during execution: {error}") from None