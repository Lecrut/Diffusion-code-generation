import re

def validate_input(text):
    if not isinstance(text, str) or text.strip() == '':
        raise ValueError("Input must be a non-empty string")

def count_word_frequencies(text):
    validate_input(text)
    words = re.findall(r'\b\w+\b', text.lower())
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with numbers 123 and symbols @#$."
    result = count_word_frequencies(sample_text)
    print(f"Input: '{sample_text}'")
    print(f"Output: {result}")