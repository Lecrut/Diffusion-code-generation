def build_dictionary(text):
    words = text.lower().split()
    frequency_dict = {}
    for word in words:
        if word:
            frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy fox The fox is quick"
    result = build_dictionary(sample_text)
    print(result)