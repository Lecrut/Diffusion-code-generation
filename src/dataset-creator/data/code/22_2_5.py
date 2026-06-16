import sys
def delete_char_at_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if not isinstance(text, str):
        raise TypeError("Text input must be a string.")
    if text is None:
        raise ValueError("Text cannot be null.")
    if index < 0 or index >= len(text):
        raise IndexError(f"Index {index} is out of bounds for the given length ({len(text)}).")
    return text[:index] + text[index+1:]
if __name__ == '__main__':
    sample_text = "Python Programming"
    target_index = 6
    try:
        result = delete_char_at_index(sample_text, target_index)
        print(f"Original: {sample_text}")
        print(f"Index to remove: {target_index}")
        print(f"Result:   '{result}'")
    except (TypeError, ValueError, IndexError) as e:
        error_message = str(e)
        if "index out of bounds" in error_message.lower():
            sys.exit(1)
        else:
            raise