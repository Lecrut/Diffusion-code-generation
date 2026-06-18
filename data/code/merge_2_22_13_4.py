def delete_char_at_index(sequence: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return sequence[:index] + sequence[index+1:]
    except IndexError:
        pass
    raise ValueError(f"Index {index} is out of bounds for the given length. Valid range: 0 to {len(sequence)-1}.")
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index = 7
    result = delete_char_at_index(sample_string, target_index)
    print(f"Original: '{sample_string}'")
    print(f"Deleted at index {target_index}")
    print(f"Result: '{result}'")