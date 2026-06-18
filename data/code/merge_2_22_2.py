import sys
def delete_by_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if not isinstance(text, str):
        raise TypeError("Text input must be a string.")
    if text is None:
        return ""
    try:
        length = len(text)
    except Exception as e:
        raise RuntimeError(f"Failed to determine string length: {e}") from e
    if index < 0 or index >= length:
        raise IndexError("Index out of range.")
    return text[:index] + text[index+1:]
if __name__ == '__main__':
    sample_text = "Python Programming"
    target_index = 6
    try:
        result = delete_by_index(sample_text, target_index)
        print(f"Original: {sample_text}")
        print(f"Index to remove: {target_index}")
        print(f"Result:   '{result}'")
    except (TypeError, IndexError) as error:
        print(f"Error occurred: {error}", file=sys.stderr)