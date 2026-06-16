def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
if __name__ == '__main__':
    test_string = "Python"
    target_index = 3
    if not isinstance(target_index, int):
        raise TypeError("Invalid index type provided.")
    try:
        result = delete_char_at_index(test_string, target_index)
        print(f"Original String: {test_string}")
        print(f"Deleted Character at Index {target_index}: 'o'")
        print(f"Modified String: {result}")
    except IndexError as e:
        raise Exception("Index out of range.") from e