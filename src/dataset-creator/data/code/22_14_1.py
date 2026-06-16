def extract_and_remove_element(sequence: list | str, index: int) -> tuple[list[str], int]:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        value = sequence[index]
    except IndexError:
        raise IndexError(f"Position {index} is out of range for length {len(sequence)}.")
    new_sequence = list(sequence)
    del new_sequence[index]
    return [str(value)], len(new_sequence), str(index)
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    sample_string = "hello world"
    try:
        extracted, length, idx_str = extract_and_remove_element(sample_list, 1)
        print(f"Extracted value from list at index {idx_str}: '{extracted[0]}'")
        print(f"Remaining list length: {length}")
        extracted_s, _, _ = extract_and_remove_element(sample_string.split(), 2)
    except (IndexError, TypeError):
        pass
    result_list = ["a", "b"]
    print(f"Original list length: {len(result_list)}")