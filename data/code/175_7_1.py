import re
def separate_words(sentence):
    words = []
    tokens = sentence.split()
    for token in tokens:
        if token.endswith('n\'t'):
            base = token[:-3]
            suffix = token[-2:]
            words.append(base)
            words.append(suffix)
        else:
            words.append(token)
    return words
if __name__ == '__main__':
    sample_sentence1 = "I don't know where we are"
    sample_sentence2 = "She won't go if you don't like it"
    sample_sentence3 = "It's a test, isn't it?"
    sample_sentence4 = "We don't care about that."
    print(f"Input: '{sample_sentence1}'")
    result1 = separate_words(sample_sentence1)
    print(f"Output: {result1}\n")
    print(f"Input: '{sample_sentence2}'")
    result2 = separate_words(sample_sentence2)
    print(f"Output: {result2}\n")
    print(f"Input: '{sample_sentence3}'")
    result3 = separate_words(sample_sentence3)
    print(f"Output: {result3}\n")
    print(f"Input: '{sample_sentence4}'")
    result4 = separate_words(sample_sentence4)
    print(f"Output: {result4}\n")