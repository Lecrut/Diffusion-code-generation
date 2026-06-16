def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
if __name__ == '__main__':
    sample_string = "Hello World"
    target_index = 5
    if not (0 <= target_index < len(sample_string)):
        raise ValueError(f"Index {target_index} is out of range for string '{sample_string}'.")
    result = delete_char_at_index(sample_string, target_index)
    print(result)