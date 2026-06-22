def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return len(text.split())

if __name__ == '__main__':
    sample_string1 = "This is a test sentence with multiple spaces."
    sample_string2 = "  leading and trailing spaces   \tand newlines\n"
    sample_string3 = ""
    sample_string4 = "OneWord"
    sample_string5 = "word1  word2\tword3"
    
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")