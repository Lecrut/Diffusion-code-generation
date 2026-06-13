import re
def extract_words(text):
    return re.findall(r'[a-zA-Z]+', text)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading spaces and trailing ones   \tmultiple\nnewlines "
    sample_string3 = "One-two-three, four five six."
    result1 = extract_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}\n")
    result2 = extract_words(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: {result2}\n")
    result3 = extract_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}\n")