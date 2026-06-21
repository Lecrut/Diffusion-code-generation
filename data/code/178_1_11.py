import re

def extract_words(text):
    return re.findall(r'\b[a-zA-Z]+\b', text)

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading space and trailing spaces   \t multiple\nnewlines "
    sample_string3 = "One-two-three four five six"
    
    result1 = extract_words(sample_string1)
    print(f"'{sample_string1}' -> {result1}")
    
    result2 = extract_words(sample_string2)
    print(f"'{sample_string2}' -> {result2}")
    
    result3 = extract_words(sample_string3)
    print(f"'{sample_string3}' -> {result3}")