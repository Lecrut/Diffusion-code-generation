def delete_char_at_index(s: str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        s = list(s)
        del s[index]
        print(''.join(s))
    except IndexError as e:
        print(f"Invalid index {index}: {e}")
if __name__ == '__main__':
    test_string = "Python Programming"
    delete_char_at_index(test_string, 0)
    delete_char_at_index(test_string, -1)