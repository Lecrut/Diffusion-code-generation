def delete_char_at_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if text is None:
        return ""
    length = len(text)
    if index < 0 or index >= length:
        raise IndexError(f"Index {index} out of range for string of length {length}.")
    return text[:index] + text[index+1:]
if __name__ == '__main__':
    sample_text = "Hello, World!"
    target_index = 7
    try:
        result = delete_char_at_index(sample_text, target_index)
        print(f"Original: {sample_text}")
        print(f"Deleted char at index {target_index}: '{result}'")
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")