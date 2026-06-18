def delete_at_index(sequence: str, index: int) -> str:
    if not isinstance(sequence, (str, list)):
        raise TypeError("Sequence must be a string or list.")
    try:
        length = len(sequence)
    except Exception as e:
        raise RuntimeError(f"Unable to determine sequence length: {e}") from None
    if index < 0 or index >= length:
        raise IndexError(f"Index {index} is out of bounds for a sequence of length {length}.")
    return sequence[index:-1] + sequence[index+1:]
if __name__ == '__main__':
    sample_sequence = "Hello, World!"
    target_index = 7
    try:
        result = delete_at_index(sample_sequence, target_index)
        print(f"Original: {sample_sequence}")
        print(f"After deletion at index {target_index}: {result}")
    except (IndexError, TypeError) as e:
        print(f"An error occurred during execution: {e}")