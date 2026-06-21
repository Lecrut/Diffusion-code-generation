def get_nth_element(text, index):
    length = len(text)
    if length == 0:
        return None
    normalized_index = index % length
    if normalized_index < 0:
        normalized_index += length
    return text[normalized_index]

if __name__ == '__main__':
    sample_string = "Hello World"
    print(get_nth_element(sample_string, 0))
    print(get_nth_element(sample_string, -1))
    print(get_nth_element(sample_string, -12))
    print(get_nth_element(sample_string, 5))
    print(get_nth_element(sample_string, -5))
    print(get_nth_element(sample_string, 100))
    print(get_nth_element(sample_string, -100))