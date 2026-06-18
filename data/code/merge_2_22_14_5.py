def extract_and_remove_element(sequence: list | str, index: int) -> tuple[list[str], int]:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        value = sequence[index]
    except IndexError:
        return [], -1
    new_sequence = list(sequence)
    del new_sequence[index]
    return [str(value)], len(new_sequence)
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    sample_string = "hello world"
    extracted_value, removed_count = extract_and_remove_element(sample_list, 1)
    print(f"List after removal: {sample_list}")
    print(f"Extracted value from list: {extracted_value[0]}")
    extracted_value_str, _ = extract_and_remove_element(sample_string, 5)
    print(f"String result (treated as sequence): '{extracted_value_str}'")