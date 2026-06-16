def append_element_to_list(existing_list: list, new_element) -> None:
    if not isinstance(existing_list, list):
        raise TypeError(f"Expected a 'list' object, got {type(existing_list).__name__}")
    existing_list.append(new_element)
if __name__ == '__main__':
    initial_data = [10, 20, 30]
    try:
        append_element_to_list(initial_data, "new_item")
        print(f"Success. Updated list: {initial_data}")
        tuple_input = (5, 6)
        if not isinstance(tuple_input, list):
            try:
                append_element_to_list(tuple_input, "should_fail")
            except TypeError as e:
                print(f"Correctly caught error for non-list input: {e}")
    except Exception as unexpected_error:
        print(f"Unexpected runtime error occurred: {unexpected_error}")