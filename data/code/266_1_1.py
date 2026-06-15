def count_words(text):
    words = text.split()
    return len(words)
if __name__ == '__main__':
    sample_string1 = "This is a sample sentence"
    sample_string2 = "  leading and trailing spaces are handled correctly "
    sample_string3 = ""
    sample_string4 = "OneWord"
    sample_string5 = "Multiple   spaces   between words"
    print(f"'{sample_string1}' has {count_words(sample_string1)} words")
    print(f"'{sample_string2}' has {count_words(sample_string2)} words")
    print(f"'{sample_string3}' has {count_words(sample_string3)} words")
    print(f"'{sample_string4}' has {count_words(sample_string4)} words")
    print(f"'{sample_string5}' has {count_words(sample_string5)} words")