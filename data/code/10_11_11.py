def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "  Hello   world  from  Python  "
    result = reverse_words_in_sentence(sample_sentence)
    print(result)