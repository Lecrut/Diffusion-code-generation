def delete_char_at_index(sequence: str, index: int) -> str:
    if not isinstance(sequence, (str, list)):
        raise TypeError("Sequence must be a string or list.")
    try:
        return sequence[index] + sequence[:index] + sequence[index+1:]
    except IndexError as e:
        print(f"Error: Index {index} is out of bounds for the given length ({len(sequence)}).", file=__import__('sys').stderr)
        raise
if __name__ == '__main__':
    sample_sequence = "Hello, World!"
    target_index = 7
    try:
        result = delete_char_at_index(sample_sequence, target_index)
        print(f"Original: {sample_sequence}")
        print(f"Modified: {result}")
    except IndexError as e:
        pass