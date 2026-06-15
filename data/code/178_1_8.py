import re
def extract_words(text):
    return re.findall(r'[a-zA-Z]+', text)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading space and trailing spaces   \tmultiple   spaces \n here. "
    sample_string3 = "One-two-three four five six"
    result1 = extract_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}")
    result2 = extract_words(sample_string2)
    print(f"Input: '{sample_string2.replace(' ', ' ').replace('\t', ' ').replace('\n', ' ')}' (cleaned for display)")
    print(f"Output: {result2}")
    result3 = extract_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}")