def first_char_of_words(text):
    if not text:
        return ""
    words = text.split()
    result = ""
    for word in words:
        if word:
            result += word[0]
    return result
if __name__ == '__main__':
    sample1 = "  Hello world  this is a test "
    sample2 = ""
    sample3 = "singleword"
    sample4 = "   leading spaces and multiple    spaces"
    sample5 = "word1  word2\tword3"
    print(f"'{sample1}' -> '{first_char_of_words(sample1)}'")
    print(f"'{sample2}' -> '{first_char_of_words(sample2)}'")
    print(f"'{sample3}' -> '{first_char_of_words(sample3)}'")
    print(f"'{sample4}' -> '{first_char_of_words(sample4)}'")
    print(f"'{sample5}' -> '{first_char_of_words(sample5)}'")