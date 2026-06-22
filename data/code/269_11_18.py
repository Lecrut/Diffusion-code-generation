import string

PUNCTUATION_CHARS = set(string.punctuation)

def extract_punctuation(text):
    punctuation_dict = {}
    for char in text:
        if char in PUNCTUATION_CHARS:
            punctuation_dict[char] = punctuation_dict.get(char, 0) + 1
    return punctuation_dict

if __name__ == '__main__':
    sample_string1 = "Hello, world! How are you?"
    sample_string2 = "This is a test string with numbers 123 and symbols @#$."
    sample_string3 = "No punctuation here."
    
    result1 = extract_punctuation(sample_string1)
    print(f"Punctuation in '{sample_string1}': {result1}")
    
    result2 = extract_punctuation(sample_string2)
    print(f"Punctuation in '{sample_string2}': {result2}")
    
    result3 = extract_punctuation(sample_string3)
    print(f"Punctuation in '{sample_string3}': {result3}")