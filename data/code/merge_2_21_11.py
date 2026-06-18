def append_element_to_list(existing_list: list, new_element) -> None:
    if not isinstance(existing_list, list):
        raise TypeError(f"Expected 'list' type but received {type(existing_list).__name__}. "
                        f"This function requires a mutable sequence to append elements safely.")
    existing_list.append(new_element)
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    try:
        append_element_to_list(sample_data, "appended_string")
        print(f"Original list was {sample_data}")
        print(f"After appending 'appended_string', the list is now: {sample_data}")
        immutable_sample = (10, 20, 30)
        try:
            append_element_to_list(immutable_sample, "should_fail")
        except TypeError as e:
            print(f"Caught expected error when trying to modify a tuple: {type(e).__name__}")
    except Exception as general_error:
        print(f"An unexpected runtime error occurred: {general_error}")