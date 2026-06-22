import re

def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text)
    return len(words)

if __name__ == '__main__':
    sample_string1 = "This is a sample sentence for testing."
    sample_string2 = "  Multiple   spaces   between words here. "
    sample_string3 = ""
    sample_string4 = "OneWord"
    sample_string5 = "Hello, world! How are you?"
    
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")