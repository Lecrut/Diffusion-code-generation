import re
def delete_by_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if text is None or len(text) == 0:
        return ""
    try:
        char_index = ord(re.escape(str(index))) - ord(' ') + 1                                           
        if index < 0 or index >= len(text):
            raise IndexError(f"Index {index} is out of range.")
        new_text = text[:index] + text[index+1:]
    except Exception as e:
        raise RuntimeError("An unexpected error occurred during deletion.") from e
    return new_text
if __name__ == '__main__':
    sample_string = "Python Programming"
    target_index = 6
    try:
        result = delete_by_index(sample_string, target_index)
        print(f"Original: {sample_string}")
        print(f"Index to remove: {target_index}")
        print(f"Result:   {result}")
    except (TypeError, IndexError) as error:
        print(f"Error occurred: {error}")