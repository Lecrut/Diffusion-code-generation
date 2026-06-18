def remove_char_at_index(text: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(text)
    if index < 0 or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    text_list = list(text)
    del text_list[index]
    print("".join(text_list))
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index = 7
    try:
        remove_char_at_index(sample_string, target_index)
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")