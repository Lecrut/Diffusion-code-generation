def delete_character_at_index(text: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        text = list(text)
        length = len(text)
        if index < 0 or index >= length:
            raise IndexError(f"Index {index} is out of range. Valid range is -{length} to {length-1}.")
        del text[index]
    except Exception as e:
        print(f"An error occurred while deleting the character at index {index}: {e}")
if __name__ == '__main__':
    sample_string = "Hello, World!"
    delete_character_at_index(sample_string, 5)
    try:
        delete_character_at_index(sample_string, -10)
    except Exception as e:
        print(f"Caught expected error for invalid negative index: {e}")
    sample_string = "Hello, World!"
    try:
        delete_character_at_index(sample_string, "5")
    except Exception as e:
        print(f"Caught expected error for invalid index type: {e}")