def extract_and_remove_element(sequence: list | str, index: int) -> tuple[list[str], int]:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        value = sequence[index]
    except IndexError:
        raise IndexError(f"Position {index} is out of range for a collection with length {len(sequence)}.")
    new_sequence = list(sequence) if isinstance(sequence, str) else sequence[:]
    del new_sequence[index]
    return [value], new_sequence
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    sample_string = "hello world"
    try:
        extracted_value, modified_list = extract_and_remove_element(sample_list, 1)
        print(f"Extracted value from list: {extracted_value}")
        print(f"Modified list: {modified_list}")
        extracted_char, modified_str = extract_and_remove_element(sample_string, 5)
        print(f"Extracted character from string: '{extracted_char}'")
        print(f"Modified string: {modified_str}")
    except (IndexError, TypeError) as e:
        print(f"An error occurred: {e}")