def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_string_1 = "This is a sample string with various spaces."
    sample_string_2 = "  leading and trailing spaces   \tand multiple spaces\n\nbetween them."
    sample_string_3 = "SingleWord"
    sample_string_4 = ""
    sample_string_5 = "  \t \n "
    
    print(f"'{sample_string_1}': {count_words(sample_string_1)}")
    print(f"'{sample_string_2}': {count_words(sample_string_2)}")
    print(f"'{sample_string_3}': {count_words(sample_string_3)}")
    print(f"'{sample_string_4}': {count_words(sample_string_4)}")
    print(f"'{sample_string_5}': {count_words(sample_string_5)}")