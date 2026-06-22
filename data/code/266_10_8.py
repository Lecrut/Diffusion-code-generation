def count_words(text):
    WORD_DELIMITERS = " \t\n\r"
    word_count = 0
    in_word = False
    
    for char in text:
        if char in WORD_DELIMITERS:
            if in_word:
                word_count += 1
                in_word = False
        else:
            in_word = True
            
    if in_word:
        word_count += 1
        
    return word_count

if __name__ == '__main__':
    sample_string1 = "This is a sample string with varying amounts of whitespace."
    sample_string2 = "  leading and trailing spaces   and multiple    spaces in between. "
    sample_string3 = "SingleWord"
    sample_string4 = ""
    sample_string5 = "  \t\n\r"
    
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")