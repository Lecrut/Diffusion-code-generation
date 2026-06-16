def append_element_to_list(existing_elements: list, new_value) -> None:
    try:
        existing_list = list(existing_elements)
        existing_list.append(new_value)
    except Exception as e:
        raise RuntimeError(f"Failed to append element due to input type error: {e}")
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    item_to_add = "new_item"
    try:
        append_element_to_list(sample_data, item_to_add)
        print("Updated list:", sample_data)
    except Exception as error:
        print(f"An unexpected error occurred: {error}")