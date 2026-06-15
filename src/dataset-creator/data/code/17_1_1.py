import re
def build_dictionary(text):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox and dog are friends."
    result = build_dictionary(sample_text)
    print(result)