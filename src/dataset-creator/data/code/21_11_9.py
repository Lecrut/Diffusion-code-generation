def append_element_to_list(existing_list: list, new_element) -> None:
    if not isinstance(existing_list, list):
        raise TypeError(f"Expected 'list' type but got {type(existing_list).__name__}")
    working_copy = existing_list.copy()
    try:
        working_copy.append(new_element)
        existing_list.clear()
        existing_list.extend(working_copy)
    except Exception as e:
        raise RuntimeError(f"Failed to append element due to {type(e).__name__}: {str(e)}") from e
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    test_elements = ["string", {"key": "value"}, (4, 5)]
    append_element_to_list(sample_data, test_elements[0])
    print(f"After appending string: {sample_data}")
    sample_data.clear()
    sample_data.extend([10, 20])
    original_nested = [[1], [2]]
    append_element_to_list(original_nested, {"nested": "dict"})
    print(f"After appending dict: {original_nested}")