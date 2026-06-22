import re

def count_word_frequencies(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text.lower())
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with numbers 123 and symbols @#$."
    result = count_word_frequencies(sample_text)
    print(f"Input: '{sample_text}'")
    print(f"Output: {result}")