def remove_char_at_index(s: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(s)
    if index < -length or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    s_list = list(s)
    offset = 0 if index > 0 else -(len(index)) + 1
    try:
        del s_list[offset]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of bounds for string.") from e
if __name__ == '__main__':
    sample_string = "Hello, World!"
    test_cases = [
        (0), 
        (-1), 
        7, 
        -8, 
        len(sample_string) + 5,
        None,
        3.5
    ]
    for idx in test_cases:
        try:
            remove_char_at_index(sample_string, idx)
        except (TypeError, IndexError):
            print(f"Error occurred with index {idx}:")