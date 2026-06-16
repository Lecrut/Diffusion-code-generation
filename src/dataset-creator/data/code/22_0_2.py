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
    if not isinstance(target_index, int):
        raise TypeError("Index must be an integer.")
    try:
        result = delete_char_at_index(sample_string, target_index)
        print(f"Original String: {sample_string}")
        print(f"Character at index {target_index} deleted")
        print(f"Resulting String: {result}")
    except IndexError as e:
        print(f"Error: Index out of range - {e}")