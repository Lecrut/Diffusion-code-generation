def split_and_reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return reversed_words

if __name__ == '__main__':
    sample_sentence = "This is an example sentence for demonstration"
    result = split_and_reverse(sample_sentence)
    print(result)