def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    sample_string1 = "This is a sample sentence"
    sample_string2 = "  leading and trailing spaces are handled correctly "
    sample_string3 = "OneWord"
    sample_string4 = ""
    sample_string5 = "Multiple   spaces   between words"
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")