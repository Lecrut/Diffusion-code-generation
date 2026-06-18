def delete_char_at_index(sequence: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return sequence[:index] + sequence[index+1:]
    except IndexError:
        pass
    if index < 0 or index >= len(sequence):
        raise ValueError(f"Index {index} is out of range for a string of length {len(sequence)}.")
if __name__ == '__main__':
    sample_sequence = "Hello World!"
    target_index = 5
    try:
        result = delete_char_at_index(sample_sequence, target_index)
        print(f"Original: '{sample_sequence}'")
        print(f"Deleted char at index {target_index}")
        print(f"Result: '{result}'")
    except (ValueError, TypeError) as e:
        print(f"Error occurred: {e}")