def separate_words(text):
    import re
    words = re.findall(r'\b\w+\b', text)
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "Python programming is fun; let's learn more."
    sample_string3 = "  Leading and trailing spaces are handled correctly.  "
    print(f"'{sample_string1}' -> {separate_words(sample_string1)}")
    print(f"'{sample_string2}' -> {separate_words(sample_string2)}")
    print(f"'{sample_string3}' -> {separate_words(sample_string3)}")