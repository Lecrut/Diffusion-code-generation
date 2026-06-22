import string

def find_unique_punctuation(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    punctuation = set(char for char in text if char in string.punctuation)
    return list(punctuation)

if __name__ == '__main__':
    sample_string1 = "Hello, world! This is a test string."
    sample_string2 = "Python3.10 is great!"
    sample_string3 = "NoPunctuationHere"
    sample_string4 = "!@#$%^&*()_+=-`~"
    
    result1 = find_unique_punctuation(sample_string1)
    print(f"String: '{sample_string1}'")
    print(f"Punctuation: {result1}")
    
    result2 = find_unique_punctuation(sample_string2)
    print(f"String: '{sample_string2}'")
    print(f"Punctuation: {result2}")
    
    result3 = find_unique_punctuation(sample_string3)
    print(f"String: '{sample_string3}'")
    print(f"Punctuation: {result3}")
    
    result4 = find_unique_punctuation(sample_string4)
    print(f"String: '{sample_string4}'")
    print(f"Punctuation: {result4}")