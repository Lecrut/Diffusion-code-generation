def delete_char_at_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(text):
        return text
    return text[:index] + text[index+1:]
if __name__ == '__main__':
    sample_text = "Python Programming"
    target_index = 6
    result = delete_char_at_index(sample_text, target_index)
    print(result)