def split_string_no_regex(text):
    result = []
    current_word = ""
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            current_word += char
        else:
            if current_word:
                result.append(current_word)
                current_word = ""
    if current_word:
        result.append(current_word)
    return result
if __name__ == '__main__':
    sample_text1 = "Hello world, this is a test."
    sample_text2 = "performance optimization example 123"
    sample_text3 = "multiple   spaces here"
    sample_text4 = "wordwithno_spaces"
    print(f"'{sample_text1}' -> {split_string_no_regex(sample_text1)}")
    print(f"'{sample_text2}' -> {split_string_no_regex(sample_text2)}")
    print(f"'{sample_text3}' -> {split_string_no_regex(sample_text3)}")
    print(f"'{sample_text4}' -> {split_string_no_regex(sample_text4)}")