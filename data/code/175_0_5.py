def separate_words(text):
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, how are you?"
    sample_string_2 = "Python is fun; let's learn about regex."
    sample_string_3 = "  Multiple   spaces and  punctuation!!! "
    print(separate_words(sample_string_1))
    print(separate_words(sample_string_2))
    print(separate_words(sample_string_3))