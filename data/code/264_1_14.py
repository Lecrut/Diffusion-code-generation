import re

def count_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

if __name__ == '__main__':
    sample_string = "Hello world! This is a test string with numbers 123 and symbols @#$."
    result = count_word_frequencies(sample_string)
    print(result)