def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_string1 = "This is a sample sentence"
    sample_string2 = "  leading and trailing spaces are handled correctly "
    sample_string3 = ""
    sample_string4 = "OneWord"
    sample_string5 = "Multiple   spaces   between words"
    
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")