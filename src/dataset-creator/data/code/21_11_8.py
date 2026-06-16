def append_element_to_list(target_list: list, new_element) -> None:
    try:
        mutable_target = list(target_list)
    except Exception as e:
        raise TypeError(f"Input must support iteration and conversion to list. Error occurred: {e}") from e
    if not isinstance(mutable_target, list):
        mutable_target = [target_list]
    try:
        mutable_target.append(new_element)
    except Exception as append_error:
        raise RuntimeError(f"Failed to append element {new_element} due to error: {append_error}") from append_error
if __name__ == '__main__':
    original_list = [1, 2, 3]
    try:
        append_element_to_list(original_list, "new_item")
        print(f"Original list after appending 'new_item': {original_list}")
        tuple_input = (4, 5)
        original_tuple = [10]
        append_element_to_list(original_tuple, "six")
        print(f"Original list after appending 'six' from tuple-like source: {original_tuple}")
    except Exception as runtime_error:
        raise runtime_error