def extract_remove_element(sequence: list | str, index: int) -> tuple[list[str], int]:
    if not isinstance(index, (int, float)):
        raise TypeError("Index must be a numeric value.")
    try:
        item = sequence[index]
    except IndexError:
        raise IndexError(f"Position {index} is out of range for length {len(sequence)}.")
    new_sequence = list(sequence) if isinstance(sequence, str) else list(sequence)
    del new_sequence[index]
    return [str(item)], len(new_sequence), new_sequence
if __name__ == '__main__':
    sample_list: list[str | int] = ["apple", "banana", 42, "cherry"]
    target_index: int = 1
    extracted_value, remaining_length, updated_collection = extract_remove_element(sample_list, target_index)
    print(f"Extracted value at index {target_index}: '{extracted_value[0]}'")
    print(f"Remaining length: {remaining_length}")
    sample_str: str = "Hello World!"
    string_target_index: int = 5
    extracted_string, remaining_len, updated_str = extract_remove_element(sample_str, string_target_index)
    print(f"\nExtracted value from string at index {string_target_index}: '{extracted_string[0]}'")
    print(f"Remaining length of modified sequence: {remaining_len}")