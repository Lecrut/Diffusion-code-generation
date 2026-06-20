def contains_special_characters(text):
    start = 33
    end = 126
    for char in text:
        code = ord(char)
        if code < start or code > end:
            return True
    return False

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Hello! World?"
    sample_string_3 = "Safe123"
    sample_string_4 = "Danger@#"
    print(contains_special_characters(sample_string_1))
    print(contains_special_characters(sample_string_2))
    print(contains_special_characters(sample_string_3))
    print(contains_special_characters(sample_string_4))