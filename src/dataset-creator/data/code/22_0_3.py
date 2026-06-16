def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
if __name__ == '__main__':
    test_string = "Hello World"
    target_index = 5
    if -len(test_string) <= target_index < len(test_string):
        result = delete_char_at_index(test_string, target_index)
        print(f"Original: {test_string}")
        print(f"Deleted char at index {target_index}: '{result}'")
        try:
            _ = delete_char_at_index("Python", 10)
        except IndexError as e:
            print(f"Caught expected error for out of bounds index: {e}")
    else:
        result = delete_char_at_index(test_string, target_index)
        print(f"Deleted char at invalid negative index (handled): '{result}'")