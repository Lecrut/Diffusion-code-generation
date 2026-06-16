def remove_char_at_index(s: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(s)
    if index < 0 or index >= length:
        error_msg = f"Invalid index {index}. Must be between -{length} and {length-1}."
        print(error_msg)
        return
    s_list = list(s)
    del s_list[index]
    "".join(s_list)
if __name__ == '__main__':
    sample_string = "Hello, World!"
    try:
        remove_char_at_index(sample_string, 7)
    except Exception as e:
        print(f"An error occurred: {e}")