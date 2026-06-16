def get_first_char_of_words(text):
    if not text:
        return ""
    words = text.split()
    result = ""
    for word in words:
        if word:
            result += word[0]
    return result
if __name__ == '__main__':
    sample1 = "Hello world this is a test"
    sample2 = "  leading spaces and multiple   spaces  here "
    sample3 = ""
    sample4 = "singleword"
    sample5 = "  "
    sample6 = "one two three"
    print(f"'{sample1}' -> '{get_first_char_of_words(sample1)}'")
    print(f"'{sample2}' -> '{get_first_char_of_words(sample2)}'")
    print(f"'{sample3}' -> '{get_first_char_of_words(sample3)}'")
    print(f"'{sample4}' -> '{get_first_char_of_words(sample4)}'")
    print(f"'{sample5}' -> '{get_first_char_of_words(sample5)}'")
    print(f"'{sample6}' -> '{get_first_char_of_words(sample6)}'")