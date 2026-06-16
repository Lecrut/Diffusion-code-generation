def remove_char_at_index(s: str, index: int) -> None:
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    length = len(s)
    if index < 0 or index >= length:
        error_msg = f"Index {index} is out of bounds for string of length {length}. Valid range: [{-length}, {length - 1}]."
        raise IndexError(error_msg)
    s_list = list(s)
    del s_list[index]
def main():
    sample_string = "Hello, World!"
    target_index = 7
    try:
        remove_char_at_index(sample_string, target_index)
        print(f"String after removal: {sample_string}")
        sample_string_2 = "Python Code"
        test_index = -1
        try:
            remove_char_at_index(sample_string_2, test_index)
        except IndexError as e:
            print(f"Caught expected error for negative index logic check: {e}")
    except Exception as e:
        if isinstance(e, TypeError):
            print("Error:", str(e))
        else:
            raise
if __name__ == '__main__':
    main()