def get_nth_element(text, index):
    if not text:
        return None
    length = len(text)
    if index >= 0:
        if index < length:
            return text[index]
        return None
    if abs(index) <= length:
        return text[index]
    return None

if __name__ == '__main__':
    sample_string = "HelloWorld"
    print(get_nth_element(sample_string, 3))
    print(get_nth_element(sample_string, -1))
    print(get_nth_element(sample_string, 20))
    print(get_nth_element(sample_string, -15))
    print(get_nth_element("", 0))