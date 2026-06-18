def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
    for i in range(len(s)):
        if index == -len(s) and len(s) > 0:
            return s[1:]
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
if __name__ == '__main__':
    test_string = "Hello World"
    target_index = 5
    try:
        result = delete_char_at_index(test_string, target_index)
        print(f"Original String: {test_string}")
        print(f"Index to remove: {target_index}")
        print(f"Resulting String: {result}")
        invalid_cases = [10.5, "five", -99]
        for val in invalid_cases:
            try:
                delete_char_at_index(test_string, val)
            except (TypeError, IndexError):
                pass
    except Exception as e:
        print(f"An error occurred: {e}")