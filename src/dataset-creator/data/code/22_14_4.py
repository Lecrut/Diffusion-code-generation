def extract_and_remove_element(sequence: list | str, index: int) -> tuple[list[str], int]:
    if not isinstance(index, (int, float)):
        raise TypeError("Index must be a number.")
    try:
        value = sequence[index]
        is_string = isinstance(sequence, str)
        processed_sequence = list(sequence)
        del processed_sequence[index]
        return (processed_sequence if not is_string else "".join(processed_sequence), value)
    except IndexError:
        raise IndexError(f"Index {index} out of range for the provided sequence.")
if __name__ == '__main__':
    sample_list = [10, 20, "apple", 40]
    sample_string = "hello world"
    list_result, removed_item = extract_and_remove_element(sample_list, 2)
    string_result, removed_char = extract_and_remove_element(sample_string, 5)
    print(f"List after removal: {list_result}")
    print(f"Removed item from list: {removed_item}")
    print(f"String after removal: '{string_result}'")
    print(f"Removed char from string: '{removed_char}'")