import re
def extract_first_letters(text):
    return re.sub(r'\b\w', lambda m: m.group(0)[0], text)
if __name__ == '__main__':
    sample_string1 = "This is a sample string for testing"
    sample_string2 = "Another example sentence here"
    sample_string3 = "word one two three"
    sample_string4 = "a b c d e"
    result1 = extract_first_letters(sample_string1)
    result2 = extract_first_letters(sample_string2)
    result3 = extract_first_letters(sample_string3)
    result4 = extract_first_letters(sample_string4)
    print(f"Input: '{sample_string1}' -> Output: '{result1}'")
    print(f"Input: '{sample_string2}' -> Output: '{result2}'")
    print(f"Input: '{sample_string3}' -> Output: '{result3}'")
    print(f"Input: '{sample_string4}' -> Output: '{result4}'")