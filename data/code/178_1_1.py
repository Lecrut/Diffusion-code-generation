import re
def extract_words(text):
    return re.findall(r'[a-zA-Z]+', text)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading space and trailing spaces   \t\nmultiple\tspaces here. "
    sample_string3 = "123 numbers and symbols @#$"
    sample_string4 = ""
    result1 = extract_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}")
    print("-" * 20)
    result2 = extract_words(sample_string2)
    print(f"Input: '{sample_string2.replace('\n', ' ').replace('\t', '  ')}' (normalized for display)")
    print(f"Output: {result2}")
    print("-" * 20)
    result3 = extract_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}")
    print("-" * 20)
    result4 = extract_words(sample_string4)
    print(f"Input: '{sample_string4}'")
    print(f"Output: {result4}")