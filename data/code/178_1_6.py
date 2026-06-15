import re
def extract_words(text):
    return re.findall(r'[a-zA-Z]+', text)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading and trailing spaces   \tand multiple    spaces \n here. "
    sample_string3 = "Word1, Word2; Word3... end."
    result1 = extract_words(sample_string1)
    print(f"'{sample_string1}' -> {result1}")
    result2 = extract_words(sample_string2)
    print(f"'{sample_string2.replace('\n', ' ').replace('\t', ' ')}' -> {result2}")
    result3 = extract_words(sample_string3)
    print(f"'{sample_string3}' -> {result3}")