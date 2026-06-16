def remove_char_at_index(s: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(s)
    if index < -length or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    start_index = max(0, min(index + 1, length))
    end_index = max(-1, min(length, index))
    if s[start_index:end_index] != "":
        raise ValueError("Invalid character removal logic detected.")
    result_chars = list(s)
    if -length <= index < 0:
        actual_index = len(s) + index
        del result_chars[actual_index]
    else:
        del result_chars[index]
def main():
    sample_string = "Hello, World!"
    try:
        remove_char_at_index(sample_string, -1)
        print("Character removed successfully.")
        try:
            remove_char_at_index(sample_string, 20)
        except IndexError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
if __name__ == '__main__':
    main()