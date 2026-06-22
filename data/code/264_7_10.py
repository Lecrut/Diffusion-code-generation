def word_length_dictionary(text: str) -> dict:
    words = text.split()
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    return length_dict

if __name__ == '__main__':
    sample_text = "Hello world! This is a test, how are you?"
    result = word_length_dictionary(sample_text)
    print(result)