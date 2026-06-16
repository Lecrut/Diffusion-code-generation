def append_element_to_list(existing_list: list, new_element) -> None:
    if not isinstance(existing_list, list) or not existing_list.__class__.__name__ == "list":
        raise TypeError("The input must be an actual Python list.")
    try:
        existing_list.append(new_element)
    except Exception as e:
        print(f"Warning: Append operation encountered a specific error: {e}")
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    try:
        append_element_to_list(sample_data, "new_item")
        print(f"Updated list content: {sample_data}")
    except TypeError as te:
        print(f"Input validation failed due to type error: {te}")