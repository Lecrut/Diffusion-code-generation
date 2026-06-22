def extract_first_words(sentence_list):
    first_words = []
    for sentence in sentence_list:
        words = sentence.split()
        if words:
            first_words.append(words[0])
    return first_words

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Learning Python is exciting and rewarding",
        "Data structures and algorithms in depth"
    ]
    extracted_words = extract_first_words(sample_sentences)
    print(extracted_words)