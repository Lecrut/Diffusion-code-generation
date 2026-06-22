def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return len(text.split())

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