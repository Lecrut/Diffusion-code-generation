def get_nth_element(s: str, n: int) -> str:
    length = len(s)
    if length == 0:
        raise IndexError("string index out of range")
    if n < 0:
        normalized_index = length + n
        if normalized_index < 0:
            raise IndexError("string index out of range")
    else:
        normalized_index = n
        if normalized_index >= length:
            raise IndexError("string index out of range")
    return s[normalized_index]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    positive_index = 7
    negative_index = -2
    print(get_nth_element(sample_string, positive_index))
    print(get_nth_element(sample_string, negative_index))