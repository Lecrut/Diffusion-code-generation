def word_lengths(text):
    words = text.split()
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    return length_dict

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    result = word_lengths(sample_text)
    print(result)