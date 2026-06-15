def separate_words(text):
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "Python is fun; let's learn about it... and more."
    sample_string3 = "  Multiple   spaces and  punctuation!!! "
    print(separate_words(sample_string1))
    print(separate_words(sample_string2))
    print(separate_words(sample_string3))