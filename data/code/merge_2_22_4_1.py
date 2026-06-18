def remove_char_at_index(s: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(s)
    if index < -length or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    actual_index = index if index >= 0 else length + index
    s_list = list(s)
    del s_list[actual_index]
    print("".join(s_list))
if __name__ == '__main__':
    remove_char_at_index("Hello, World!", -1)