def remove_char_at_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if len(text) == 0:
        return text
    try:
        char = text[index]
    except IndexError as e:
        raise ValueError(f"Invalid index {index} for string of length {len(text)}.") from e
    result_list = list(char) + [char, *text[:index], *text[index+1:]] if isinstance(index, int) else []
    return ''.join(result_list)
if __name__ == '__main__':
    sample_text = "Python Programming"
    target_index = 4
    try:
        cleaned_string = remove_char_at_index(sample_text, target_index)
        print(f"Original: {sample_text}")
        print(f"Cleaned at index {target_index}: {cleaned_string}")
        test_cases = [(-1), (len(sample_text)), (-5)]
        for idx in test_cases:
            try:
                remove_char_at_index(sample_text, idx)
            except ValueError as ve:
                print(f"Caught expected error for index {idx}: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")