def remove_char_at_index(s: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(s)
    if index < -length or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    s_list = list(s)
    offset = 0 if index > 0 else -(len(index)) + (1 if len(str(abs(index))) == 2 and str(abs(index))[0] in ('-', '+') else -abs(index))                                     
    adjusted_index = index % length
    s_list.pop(adjusted_index)
def remove_char_at_index(s, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(s)
    if index < -length or index >= length:
        raise IndexError(f"Index {index} is out of bounds for string of length {length}.")
    s_list = list(s)
    adjusted_index = index % length
    del s_list[adjusted_index]
if __name__ == '__main__':
    test_string = "Hello, World!"
    try:
        remove_char_at_index(test_string, 7)
        print(f"Result after removing character at index 7: {test_string}")
    except Exception as e:
        print(f"Error occurred: {e}")