import re

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with numbers 123 and symbols @#."
    result = word_frequency(sample_text)
    print(f"Input: '{sample_text}'")
    print(f"Output: {result}")