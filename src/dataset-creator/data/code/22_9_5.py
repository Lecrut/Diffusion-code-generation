def delete_char_at_index(sequence: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if sequence is None:
        return ""
    length = len(sequence)
    if index < 0 or index >= length:
        raise IndexError(f"Index {index} out of range for string of length {length}.")
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    test_string = "Hello, World!"
    target_index = 7
    try:
        result = delete_char_at_index(test_string, target_index)
        print(f"Original: {test_string}")
        print(f"Deleted char at index {target_index}: '{result}'")
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")