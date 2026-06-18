def delete_char_at_index(sequence: str, index: int) -> str:
    if not isinstance(sequence, (str, list)):
        raise TypeError("Sequence must be a string or list.")
    try:
        length = len(sequence)
    except Exception as e:
        raise RuntimeError(f"Failed to determine sequence length: {e}") from None
    if index < 0 or index >= length:
        return f"IndexError: Index out of bounds. Valid range is [{-length}, {length - 1}]. Provided index was {index}."
    try:
        result = sequence[:index] + sequence[index+1:]
    except Exception as e:
        raise RuntimeError(f"Failed to construct new sequence: {e}") from None
    return result
if __name__ == '__main__':
    sample_sequence = "Hello, World!"
    target_index = 7
    output_result = delete_char_at_index(sample_sequence, target_index)
    print(output_result)