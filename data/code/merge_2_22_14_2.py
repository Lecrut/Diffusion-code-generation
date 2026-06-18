def remove_element_at_index(sequence: list | str, index: int) -> None:
    if isinstance(sequence, (list, tuple)):
        del sequence[index]
    elif isinstance(sequence, str):
        chars = list(sequence)
        del chars[index]
        sequence = "".join(chars)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_string = "hello"
    remove_element_at_index(sample_list, 2)
    print(f"Modified list: {sample_list}")
    original_str = "world"
    chars = list(original_str)
    del chars[1]
    modified_string = "".join(chars)
    print(f"Modified string representation: '{modified_string}'")