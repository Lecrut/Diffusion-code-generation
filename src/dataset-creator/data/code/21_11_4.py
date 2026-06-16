def append_element_to_list(existing_list: list, new_element) -> None:
    if not isinstance(existing_list, (list)):
        raise TypeError(f"Expected a list instance but got {type(existing_list).__name__}")
    existing_list.append(new_element)
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    try:
        append_element_to_list(sample_data, "new_item")
        print(f"Success! Updated list: {sample_data}")
        invalid_input = (5, 6)                                                                             
    except TypeError as e:
        print(f"Error occurred: {e}")