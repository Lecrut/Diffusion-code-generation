import re

def replace_non_word_chars(text):
    return re.sub(r'\W+', ' ', text)

def split_text_to_words(text):
    return text.split()

def tokenize_string(text):
    replaced_text = replace_non_word_chars(text)
    words = split_text_to_words(replaced_text)
    return words

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "  Multiple   spaces and punctuation ,. ;  are handled here."
    sample_string3 = "Word1,Word2.Word3"
    sample_string4 = "  leading and trailing spaces  "
    
    print(f"Input: '{sample_string1}'")
    print(f"Tokens: {tokenize_string(sample_string1)}\n")
    
    print(f"Input: '{sample_string2}'")
    print(f"Tokens: {tokenize_string(sample_string2)}\n")
    
    print(f"Input: '{sample_string3}'")
    print(f"Tokens: {tokenize_string(sample_string3)}\n")
    
    print(f"Input: '{sample_string4}'")
    print(f"Tokens: {tokenize_string(sample_string4)}\n")