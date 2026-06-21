def tokenize_sentence(sentence, delimiter):
    return sentence.split(delimiter)

if __name__ == '__main__':
    sample_sentence = "This is another sample sentence for testing."
    delimiter = " "
    result = tokenize_sentence(sample_sentence, delimiter)
    print(result)