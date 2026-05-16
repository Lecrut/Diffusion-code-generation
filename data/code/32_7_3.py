def word_lengths_generator(sentence):
    words = sentence.split()
    for word in words:
        yield len(word)
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing"
    length_generator = word_lengths_generator(sample_sentence)
    result_list = list(length_generator)
    print(result_list)