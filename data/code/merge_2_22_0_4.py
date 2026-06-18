def delete_char(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
    raise ValueError(f"Invalid index {index} for string of length {len(s)}.")
if __name__ == '__main__':
    test_string = "Hello, World!"
    try:
        result = delete_char(test_string, 7)
        print(result)
        try:
            bad_result = delete_char(test_string, -50)
        except ValueError as ve:
            print(f"Caught expected error for negative index: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")