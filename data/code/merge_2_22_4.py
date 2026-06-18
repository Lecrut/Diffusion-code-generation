def remove_char_at_index(text: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(text)
    if index < -length or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    actual_index = index if index >= 0 else length + index
    text_list = list(text)
    del text_list[actual_index]
    "".join(text_list)
if __name__ == '__main__':
    sample_text = "Python"
    remove_char_at_index(sample_text, -1)