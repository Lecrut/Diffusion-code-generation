def delete_by_index(sequence: list | str, index: int) -> None:
    if isinstance(sequence, str):
        chars = list(sequence)
    elif isinstance(sequence, (list, tuple)):
        chars = list(sequence)
    else:
        raise TypeError("Input must be a string or sequence.")
    if not 0 <= index < len(chars):
        raise IndexError(f"Index {index} is out of range for length {len(chars)}.")
    del chars[index]
if __name__ == '__main__':
    sample_string = "hello world"
    sample_list = [1, 'a', 3.14, True]
    delete_by_index(sample_string, 5)
    print(f"Modified string: {sample_string}")
    delete_by_index(sample_list, 2)
    print(f"Modified list: {sample_list}")